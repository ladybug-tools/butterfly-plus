"""A collection of useful methods."""
try:
    import Rhino as rc
    import scriptcontext as sc
    from Grasshopper.Kernel.Types import GH_ObjectWrapper as Goo
except ImportError:
    pass

from butterfly.utilities import load_of_points_file, load_of_faces_file
import os

tolerance = sc.doc.ModelAbsoluteTolerance


def gh_wrapper(objs):
    """Put item in a Grasshopper Object Wrapper."""
    try:
        return (Goo(obj) for obj in objs)
    except Exception as e:
        raise Exception(
            'Failed to wrap butterfly object in Grasshopper wrapper:\n\t{}'.format(e))


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

    # create mesh edges
    pts = tuple(rc.Geometry.Point3d(*p) for p in pts)
    # create a closed polyline for each edge
    mesh = tuple(
        rc.Geometry.Polyline([pts[i] for i in f] + [pts[f[0]]]).ToNurbsCurve()
        for f in faces)

    # scale mesh to Rhion units if not meters
    if convertToMeters != 1:
        for m in mesh:
            m.Scale(1.0 / convertToMeters)

    return mesh


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
    return tuple(rc.Geometry.Point3d(*p) for p in pts)
