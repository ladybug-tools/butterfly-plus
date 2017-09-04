# coding=utf-8
"""RefinementRegion for Dynamo."""
from butterfly.refinementRegion import RefinementRegion
from .geometry import MeshDS


class RefinementRegionDS(RefinementRegion):
    """Butterfly refinement region in Dynamo.

    Attributes:
        name: Name as a string (A-Z a-z 0-9).
        geometries: A list of Dynamo meshes or Breps. All input geometries
            will be converted as a joined mesh.
        refinement_mode: Refinement mode (0: inside, 1: outside, 2: distance)
        meshing_parameters: Dynamo meshing parameters for meshing brep geometries.
            In case geometry is Mesh this input won't be used.
    """

    def __init__(self, name, geometries, refinement_mode, tolerance=-1,
                 max_grid_lines=512):
        """Init Butterfly geometry."""
        _mesh = MeshDS(geometries, tolerance, max_grid_lines)
        self.__geometry = _mesh.geometry
        RefinementRegion.__init__(self, name, _mesh.vertices, _mesh.face_indices,
                                  _mesh.normals, refinement_mode)
