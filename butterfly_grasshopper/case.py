# coding=utf-8
"""OpemFOAM Case for Grasshopper."""
import butterfly.case
from .utilities import load_of_mesh, load_of_points


class Case(butterfly.case.Case):
    """Butterfly case for Grasshopper."""

    def load_mesh(self, inner_mesh=True):
        """Return OpenFOAM mesh as a Rhino mesh."""
        if hasattr(self, 'blockMeshDict'):
            convert_to_meters = self.blockMeshDict.convert_to_meters
        else:
            convert_to_meters = 1

        return load_of_mesh(self.poly_mesh_folder, convert_to_meters, inner_mesh)

    def load_points(self):
        """Return OpenFOAM mesh as a Rhino mesh."""
        if hasattr(self, 'blockMeshDict'):
            convert_to_meters = self.blockMeshDict.convert_to_meters
        else:
            convert_to_meters = 1

        return load_of_points(self.poly_mesh_folder, convert_to_meters)
