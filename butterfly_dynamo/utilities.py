"""A collection of useful methods."""
try:
    import clr
    clr.AddReference('ProtoGeometry')
    import Autodesk.DesignScript.Geometry as DSGeometry
except ImportError:
    pass

import os
from butterfly.utilities import load_of_points_file, load_of_faces_file

__all__ = ('load_of_mesh', 'load_of_points')

tolerance = 0.001


def load_of_mesh(polyMesh_folder, convertToMeters=1, inner_mesh=True):
    """Convert OpenFOAM mesh to a Rhino Mesh."""
    if not polyMesh_folder:
        return

    pff = tuple(f for f in os.listdir(polyMesh_folder) if f.startswith('points'))
    fff = tuple(f for f in os.listdir(polyMesh_folder) if f.startswith('faces'))

    if pff:
        pf = os.path.join(polyMesh_folder, pff[0])
    else:
        raise ValueError('Failed to find points file at {}'.format(polyMesh_folder))
    if fff:
        ff = os.path.join(polyMesh_folder, fff[0])
    else:
        raise ValueError('Failed to find faces file at {}'.format(polyMesh_folder))

    pts = load_of_points_file(pf)
    faces = load_of_faces_file(ff, inner_mesh)

    # create the mesh
    pts = tuple(DSGeometry.Point.ByCoordinates(*p) for p in pts)
    mesh = tuple(
        DSGeometry.PolyCurve.ByPoints((pts[i] for i in f), True)
        for f in faces)

    # scale mesh to Dynamo units if not meters
    if convertToMeters != 1:
        mesh = tuple(m.Scale(1.0 / convertToMeters) for m in mesh)

    # dispose points
    for pt in pts:
        pt.Dispose()
    return mesh


def _triangulate(v):
    """return indices as tuples with of 3 vertices."""
    return ((v[0], v[i], v[i + 1]) for i in range(1, len(v) - 1))


# TODO(): Scale points based on convertToMeters
def load_of_points(polyMesh_folder, convertToMeters=1):
    """Load OpenFOAM points as Rhino points."""
    if not polyMesh_folder:
        return

    pff = tuple(f for f in os.listdir(polyMesh_folder) if f.startswith('points'))

    if pff:
        pf = os.path.join(polyMesh_folder, pff[0])
    else:
        raise ValueError('Failed to find points file at {}'.format(polyMesh_folder))

    pts = load_of_points_file(pf)
    return tuple(DSGeometry.Point.ByCoordinates(*p) for p in pts)
