# coding=utf-8
"""BF Grasshopper geometry library."""
try:
    import Rhino as rc
    from scriptcontext import doc
except ImportError:
    pass

from copy import deepcopy
from butterfly.geometry import BFGeometry


class MeshGH(object):
    """Base mesh class for Butterfly Grasshopper.

    Attributes:
        geometries: A list of Grasshopper meshes or Breps. All input geometries
            will be converted as a joined mesh.
        meshing_parameters: Grasshopper meshing parameters for meshing brep geometries.
            In case geometry is Mesh this input won't be used.
    """

    def __init__(self, geometries, meshing_parameters=None):
        """Init Butterfly geometry in Grasshopper."""
        if not meshing_parameters:
            meshing_parameters = rc.Geometry.MeshingParameters.Default

        self.__meshing_parameters = meshing_parameters
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
        _geo = rc.Geometry.Mesh()

        # if geo is not a mesh try to mesh it
        # this is useful for creating stl files
        for g in geo:
            if isinstance(g, rc.Geometry.Brep):
                for m in rc.Geometry.Mesh.CreateFromBrep(g, self.__meshing_parameters):
                    _geo.Append(m)
            elif isinstance(g, rc.Geometry.Mesh):
                _geo.Append(g)
            else:
                raise ValueError("Input geometry should be Mesh or Brep not {}"
                                 .format(type(g)))

        self.__geometry = self.__triangulate_mesh(_geo)

    @property
    def normals(self):
        """Mesh Face normals."""
        return tuple((n.X, n.Y, n.Z) for n in self.geometry.FaceNormals)

    @property
    def vertices(self):
        """Mesh Face normals."""
        return tuple((v.X, v.Y, v.Z) for v in self.geometry.Vertices)

    @property
    def face_indices(self):
        """Mesh Face Indices."""
        return tuple((f.A, f.B, f.C) for f in self.geometry.Faces)

    def __triangulate_mesh(self, mesh):
        """Triangulate Rhino Mesh."""
        tri_mesh = rc.Geometry.Mesh()

        for i in xrange(mesh.Vertices.Count):
            tri_mesh.Vertices.Add(mesh.Vertices[i])

        for face in mesh.Faces:
            tri_mesh.Faces.AddFace(face.A, face.B, face.C)
            if face.IsQuad:
                tri_mesh.Faces.AddFace(face.A, face.C, face.D)

        # collect mesh faces, normals and indices
        tri_mesh.FaceNormals.ComputeFaceNormals()
        tri_mesh.FaceNormals.UnitizeFaceNormals()
        return tri_mesh

    def duplicate(self):
        """Return a copy of GHMesh."""
        return deepcopy(self)

    def ToString(self):
        """Overwrite .NET ToString method."""
        return self.__repr__()

    def __repr__(self):
        """GHMesh."""
        return str(self.geometry)


class BFGeometryGH(BFGeometry):
    """Base geometry class for Butterfly.

    Attributes:
        name: Name as a string (A-Z a-z 0-9).
        geometries: A list of Grasshopper meshes or Breps. All input geometries
            will be converted as a joined mesh.
        boundary_condition: Boundary condition for this geometry
        meshing_parameters: Grasshopper meshing parameters for meshing brep geometries.
            In case geometry is Mesh this input won't be used.
    """

    def __init__(self, name, geometries, boundary_condition=None,
                 refinementLevels=None, nSurfaceLayers=None,
                 meshing_parameters=None):
        """Init Butterfly geometry in Grasshopper."""
        # convert input geometries to a butterfly GHMesh.
        _mesh = MeshGH(geometries, meshing_parameters)

        self.__geometry = _mesh.geometry

        BFGeometry.__init__(self, name, _mesh.vertices, _mesh.face_indices,
                            _mesh.normals, boundary_condition, refinementLevels,
                            nSurfaceLayers)

    @property
    def geometry(self):
        """Mesh geometry of the geometry."""
        return self.__geometry


class BFBlockGeometryGH(BFGeometryGH):
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

    def __init__(self, name, geometries, boundary_condition=None,
                 meshing_parameters=None):
        """Init Butterfly block geometry in Grasshopper."""
        BFGeometryGH.__init__(self, name, geometries, boundary_condition,
                              meshing_parameters=meshing_parameters)

        self.__calculate_block_border_vertices(geometries)

    @property
    def isBFBlockGeometry(self):
        """Return True for Butterfly block geometries."""
        return True

    @property
    def border_vertices(self):
        """Return list of border vertices."""
        return self.__borderVertices

    def __calculate_block_border_vertices(self, geo):
        """Get list of border vertices."""
        self.__borderVertices = []
        for g in geo:
            if not isinstance(g, rc.Geometry.Brep):
                raise TypeError('{} is not a Brep.'.format(g))

            self.__borderVertices.extend(
                tuple(tuple((v.X, v.Y, v.Z) for v in self.__get_face_border_vertices(f))
                      for f in g.Faces)
            )

    @staticmethod
    def __get_face_border_vertices(face):
        """Get border vertices."""
        srf = face.DuplicateFace(doc.ModelAbsoluteTolerance)
        edges_joined = rc.Geometry.Curve.JoinCurves(srf.DuplicateEdgeCurves(True))
        return (e.PointAtStart for e in edges_joined[0].DuplicateSegments())


def bf_mesh_to_mesh(bf_mesh, color=None, scale=1):
    """convert a BFMesh object to Grasshopper mesh."""
    assert hasattr(bf_mesh, 'vertices'), \
        '\t{} is not a valid BFMesh.'.format(bf_mesh)
    assert hasattr(bf_mesh, 'faceIndices'), \
        '\t{} is not a valid BFMesh.'.format(bf_mesh)

    mesh = rc.Geometry.Mesh()
    for v in bf_mesh.vertices:
        mesh.Vertices.Add(rc.Geometry.Point3d(*v))

    for face in bf_mesh.face_indices:
        mesh.Faces.AddFace(*face)

    if color:
        mesh.VertexColors.CreateMonotoneMesh(color)

    if scale != 1:
        mesh.Scale(scale)

    return mesh


def xyz_to_point(xyz, convert_from_meters=1):
    """Convert a xyz tuple to Point."""
    return rc.Geometry.Point3d(*(i * convert_from_meters for i in xyz))


def xyz_to_vector(xyz):
    """Convert a xyz tuple to Vector."""
    return rc.Geometry.Vector3d(*xyz)
