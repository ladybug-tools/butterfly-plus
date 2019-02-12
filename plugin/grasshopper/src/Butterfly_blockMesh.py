# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
blockMesh

-

    Args:
        _case: Butterfly case.
        _grad_xyz_: A simpleGrading (default: simpleGrading(1, 1, 1)). This value
            updates grading in blockMeshDict.
        _cell_count_: Number of cells in (x, y, z) as a Point (default: 5).
            This value updates number of divisions in blockMeshDict.
        _overwrite_: Remove current snappyHexMesh folders from the case if any (default: True). 
        _write: Updat blockMeshDict.
        run_: run blockMesh.
    Returns:
        report: Reports, errors, warnings, etc.
        case: Butterfly case.
"""

ghenv.Component.Name = "Butterfly_blockMesh"
ghenv.Component.NickName = "blockMesh"
ghenv.Component.Message = 'VER 0.0.05\nJAN_12_2019'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "03::Mesh"
ghenv.Component.AdditionalHelpFromDocStrings = "1"

if _case and _write:
    # remove current snappyHexMeshFolders
    if _overwrite_:
        _case.remove_snappyHexMesh_folders()
    # run blockMesh
    if _cell_count_:
        print('Updating cell size in blockMeshDict.')
        _case.blockMeshDict.n_div_xyz = \
            (_cell_count_.X, _cell_count_.Y, _cell_count_.Z)
    if _grad_xyz_:
        print('Updating grading in blockMeshDict.')
        _case.blockMeshDict.grading = _grad_xyz_
    if _cell_count_ or _grad_xyz_:
        path = _case.blockMeshDict.save(_case.project_dir)
        print('Saved changes to blockMeshDict to:\n{}'.format(path))
    
    if run_:
        log = _case.blockMesh(overwrite=True)
        if log.success:
            case = _case
        else:
            raise Exception("\n\n\nButterfly failed to run OpenFOAM command!\n%s" % log.error)
    else:
        # output case for next step of meshing. SnappyHexMesh component will run
        # blockMesh if it is not already created and ran.
        case = _case