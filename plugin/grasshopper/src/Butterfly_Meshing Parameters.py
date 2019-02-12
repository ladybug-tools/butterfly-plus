# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Set meshing parameters for blockMesh and snappyHexMesh.


    Args:
        _cell_size_xyz_: Cell size in (x, y, z) as a tuple (default: length / 5).
            This value updates number of divisions in blockMeshDict.
        _grad_xyz_: A simpleGrading (default: simpleGrading(1, 1, 1)). This value
            updates grading in blockMeshDict.
        _loc_in_mesh_: A tuple for the location of the mesh to be kept. This
            value updates locationInMesh in snappyHexMeshDict.
        _glob_ref_level_: A tuple of (min, max) values for global refinment.
            This value updates globalRefinementLevel in snappyHexMeshDict.
    Returns:
        report: Reports, errors, warnings, etc.
        mesh_params: meshingParameters.
"""

ghenv.Component.Name = "Butterfly_Meshing Parameters"
ghenv.Component.NickName = "meshParams"
ghenv.Component.Message = 'VER 0.0.05\nJAN_12_2019'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "00::Create"
ghenv.Component.AdditionalHelpFromDocStrings = "4"

try:
    # import butterfly
    from butterfly.meshingparameters import MeshingParameters
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

# create blockMeshDict based on BBox
if _cell_size_xyz_:
    _cell_size_xyz_ = _cell_size_xyz_.X, _cell_size_xyz_.Y, _cell_size_xyz_.Z

mesh_params = MeshingParameters(
    _cell_size_xyz_, _grad_xyz_, _loc_in_mesh_, _glob_ref_level_)
