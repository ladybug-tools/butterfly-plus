# coding=utf-8
"""OpemFOAM Case for Dynamo."""
import butterfly.case
from .utilities import load_of_mesh, load_of_points


class Case(butterfly.case.Case):
    """Butterfly case for Dynamo."""

    def load_mesh(self, inner_mesh=True):
        """Return OpenFOAM mesh as a Rhino mesh."""
        if hasattr(self, 'blockMeshDict'):
            convertToMeters = self.blockMeshDict.convertToMeters
        else:
            convertToMeters = 1

        return load_of_mesh(self.polyMesh_folder, convertToMeters, inner_mesh)

    def load_points(self):
        """Return OpenFOAM mesh as a Rhino mesh."""
        if hasattr(self, 'blockMeshDict'):
            convertToMeters = self.blockMeshDict.convertToMeters
        else:
            convertToMeters = 1

        return load_of_points(self.polyMesh_folder, convertToMeters)
