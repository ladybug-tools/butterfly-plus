# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Windtunnel auto grading

This component generates gradingXYZ for an outdoor study (wind tunnel).
-

    Args:
        _windTunnel: windTunnel iput from create case from tunnel component.
        _cellSize_: Cell size for the area of interest (default: 1).
        _cellToCellRatio_: Cell to cell expansion ratio (default: 1.2).
        wakeOffset_: The length to be added to the end of geometries bounding
            box to be considerd as part of area of interest (default: 2).
        heightOffset_: The length to be added to the topic of geometries bounding
            box to be considerd as part of area of interest (default: 5).        
        areaOfInterest_: Remove current snappyHexMesh folders from the case if any (default: True). 
    Returns:
        readMe!: Reports, errors, warnings, etc.
        gradXYZ: A butterfly Grading. Connect this output to gradXYZ in blockMesh
            component to set the grading of blockMesh in X, Y or Z direction.
        cellCount: Number of cells in XYZ directions. Connect this output to
            cellCount in blockMesh component to set the cell count of blockMesh
            in X, Y or Z direction.
        preview: An approximation of blockMesh based on gradXYZ and cellCount.
            For accurate mesh visualization run blockMesh and visualize the
            output mesh [To be implemented!].
"""

ghenv.Component.Name = "Butterfly_wind Tunnel Grading"
ghenv.Component.NickName = "WTGrading"
ghenv.Component.Message = 'VER 0.0.04\nNOV_09_2018'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "03::Mesh"
ghenv.Component.AdditionalHelpFromDocStrings = "3"

try:
    from butterfly_grasshopper.geometry import xyz_to_point
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _windTunnel:
    if areaOfInterest_:
        raise NotImplementedError(
          '\nArea of interest is not implemented yet!\nThis component uses '
          'geometry bounding box as the area of interest.\n'
          'You can use offset inputs to adjust the current bounding box.'
        )
    gradXYZ, cell_count = _windTunnel.calculate_grading(
        _cellSize_[0], _cellToCellRatio_[0], wakeOffset_, heightOffset_)
    cellCountXYZ = xyz_to_point(cell_count)
    cellCountTot = int(cellCountXYZ.X * cellCountXYZ.Y * cellCountXYZ.Z)
