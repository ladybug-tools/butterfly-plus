# coding=utf-8
"""BF Dynamo geometry library."""
try:
    import clr
    import System
    clr.AddReference('ProtoGeometry')
    import Autodesk.DesignScript.Geometry as DSGeometry
    _loc = tuple(a.Location
                 for a in System.AppDomain.CurrentDomain.GetAssemblies()
                 if 'MeshToolkit' in a.FullName)
    assert len(_loc) != 0, \
        'Failed to find MeshToolkit!\n' \
        'You need to install MeshToolkit from package maneger to use Butterfly.'

    clr.AddReferenceToFileAndPath(_loc)
    import Autodesk.Dynamo.MeshToolkit as MeshToolkit
except ImportError:
    pass

from copy import deepcopy
from butterfly.geometry import BFGeometry


class MeshDS(object):
    """Base mesh class for Butterfly Dynamo.

    Attributes:
        geometries: A list of Dynamo meshes or Breps. All input geometries
            will be converted as a joined mesh.
        meshing_parameters: A tuple for tolerance and max_grid_lines
            (default: (-1, 512)).
    """

    def __init__(self, geometries, meshing_parameters=None):
        """Init Butterfly geometry in Dynamo."""
        if not meshing_parameters:
            meshing_parameters = -1, 512
        try:
            tolerance = int(meshing_parameters[0])
            max_grid_lines = int(meshing_parameters[1])
        except Exception as e:
            msg = 'Failed to read meshing_parameters from {}:\n{}'.format(
                meshing_parameters, e
            )
            print(msg)
            tolerance = -1
            max_grid_lines = 512

        self.__tolerance = tolerance
        self.__max_grid_lines = max_grid_lines
        self.geometry = geometries

    @property
    def geometry(self):
        """Mesh geometry of the geometry."""
        return self.__geometry

    @geometry.setter
    def geometry(self, geo):
        """Geometry.

        Args:
            geo: A list of geometries
        """
        # if geo is not a mesh try to mesh it
        # this is useful for creating stl files
        _geo = []
        for g in geo:
            try:
                if not hasattr(g, 'vertices'):
                    # not a mesh
                    _geo.append(
                        MeshToolkit.Mesh.ByGeometry(
                            g, self.__tolerance, self.__max_grid_lines))
                elif hasattr(g, 'vertices'):
                    _geo.append(g)
            except Exception as e:
                raise ValueError(
                    "Failed to create a mesh from {}:\n\t{}".format(type(g), e))

        self.__geometry = self.__join_mesh(_geo)

    @property
    def normals(self):
        """Mesh Face normals."""
        return tuple((n.X, n.Y, n.Z) for n in self.geometry.TriangleNormals())

    @property
    def vertices(self):
        """Mesh Face normals."""
        return tuple((v.X, v.Y, v.Z) for v in self.geometry.Vertices())

    @property
    def face_indices(self):
        """Mesh Face Indices."""
        _ind = tuple(self.geometry.VertexIndicesByTri())
        return tuple(_ind[3 * i: 3 * i + 3] for i in range(len(_ind) / 3))

    def __join_mesh(self, mesh):
        """Join a list of meshes into a joined mesh."""
        if len(mesh) == 1:
            return mesh[0]

        # collect vertices of all the meshes
        ds_pts = (pt for m in mesh for pt in m.Vertices())
        ver_count = int(-mesh[0].VertexCount)
        ind = []
        for m in mesh:
            ver_count += int(m.VertexCount)
            ind.extend((int(i) + ver_count for i in m.VertexIndicesByTri()))

        joined_mesh = MeshToolkit.Mesh.ByVerticesAndIndices(ds_pts, ind)
        return joined_mesh

    def duplicate(self):
        """Return a copy of DSMesh."""
        return deepcopy(self)

    def to_string(self):
        """Overwrite .NET ToString method."""
        return self.__repr__()

    def __repr__(self):
        """DSMesh."""
        return str(self.geometry)


class BFGeometryDS(BFGeometry):
    """Base geometry class for Butterfly.

    Attributes:
        name: Name as a string (A-Z a-z 0-9).
        geometries: A list of Dynamo meshes or Breps. All input geometries
            will be converted as a joined mesh.
        boundary_condition: Boundary condition for this geometry
        meshing_parameters: Dynamo meshing parameters for meshing brep geometries.
            In case geometry is Mesh this input won't be used.
    """

    def __init__(self, name, geometries, boundary_condition=None,
                 refinement_levels=None, n_surface_layers=None, tolerance=-1,
                 max_grid_lines=512):
        """Init Butterfly geometry in Dynamo."""
        # convert input geometries to a butterfly DSMesh.
        _mesh = MeshDS(geometries, (tolerance, max_grid_lines))

        self.__geometry = _mesh.geometry
        # put indices in groups of three
        BFGeometry.__init__(self, name, _mesh.vertices, _mesh.face_indices,
                            _mesh.normals, boundary_condition, refinement_levels,
                            n_surface_layers)

    @property
    def geometry(self):
        """Mesh geometry of the geometry."""
        return self.__geometry


class BFBlockGeometry_DS(BFGeometryDS):
    """Butterfly block geometry.

    Use this geometry to create geometries for blockMeshDict.

    Attributes:
        name: Name as a string (A-Z a-z 0-9 _).
        vertices: A flatten list of (x, y, z) for vertices.
        faceIndices: A flatten list of (a, b, c) for indices for each face.
        normals: A flatten list of (x, y, z) for face normals.
        boundary_condition: Boundary condition for this geometry.
        borderVertices: List of lists of (x, y, z) values for each quad face of
            the geometry.
    """

    def __init__(self, name, geometries, boundary_condition=None, tolerance=-1,
                 max_grid_lines=512):
        """Init Butterfly block geometry in Dynamo."""
        BFGeometryDS.__init__(self, name, geometries, boundary_condition,
                              tolerance=tolerance, max_grid_lines=max_grid_lines)

    @property
    def is_bf_block_geometry(self):
        """Return True for Butterfly block geometries."""
        return True

    @property
    def border_vertices(self):
        """Return list of border vertices."""
        # BFBlockGeometry is planar so vertices of geometry are the same as
        # vertices of meshed geometry
        return self.geometry.vertices


# TODO(): add coloring
def bf_mesh_to_mesh(bf_mesh, color=None, scale=1):
    """convert a BFMesh object to Dynamo mesh."""
    assert hasattr(bf_mesh, 'vertices'), \
        '\t{} is not a valid BFMesh.'.format(bf_mesh)
    assert hasattr(bf_mesh, 'faceIndices'), \
        '\t{} is not a valid BFMesh.'.format(bf_mesh)

    ds_pts = (DSGeometry.Point.ByCoordinates(*p) for p in bf_mesh.vertices)
    ind = (i for face in bf_mesh.face_indices for i in face)
    mesh = MeshToolkit.Mesh.ByVerticesAndIndices(ds_pts, ind)

    if scale != 1:
        mesh.Scale(scale)

    # if color:
    #   meshDisplay = MeshDisplay.ByMeshColor(mesh, color)
    #   return meshDisplay

    return mesh


def xyz_to_point(xyz, convert_from_meters=1):
    """Convert a xyz tuple to Point."""
    return DSGeometry.Point.ByCoordinates(*(i * convert_from_meters for i in xyz))


def xyz_to_vector(xyz):
    """Convert a xyz tuple to Vector."""
    return DSGeometry.Vector.ByCoordinates(*xyz)
