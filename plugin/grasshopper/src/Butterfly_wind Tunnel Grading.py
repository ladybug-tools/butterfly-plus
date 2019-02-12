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
        _wind_tunnel: windTunnel iput from create case from tunnel component.
        _cell_size_: Cell size for the area of interest (default: 1).
        _cell_to_cell_ratio_: Cell to cell expansion ratio (default: 1.2).
        wake_offset_: The length to be added to the end of geometries bounding
            box to be considerd as part of area of interest (default: 2).
        height_offset_: The length to be added to the topic of geometries bounding
            box to be considerd as part of area of interest (default: 5).        
        area_of_interest_: Remove current snappyHexMesh folders from the case if any (default: True). 
    Returns:
        report: Reports, errors, warnings, etc.
        grad_xyz: A butterfly Grading. Connect this output to grad_xyz in blockMesh
            component to set the grading of blockMesh in X, Y or Z direction.
        cell_count_xyz: Number of cells in XYZ directions. Connect this output to
            cellCount in blockMesh component to set the cell count of blockMesh
            in X, Y or Z direction.
        cell_count_tot: Number of total cells.
        preview: An approximation of blockMesh based on grad_xyz and cellCount.
            For accurate mesh visualization run blockMesh and visualize the
            output mesh [To be implemented!].
"""

ghenv.Component.Name = "Butterfly_wind Tunnel Grading"
ghenv.Component.NickName = "WTGrading"
ghenv.Component.Message = 'VER 0.0.05\nJAN_12_2019'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "03::Mesh"
ghenv.Component.AdditionalHelpFromDocStrings = "3"

try:
    from butterfly_grasshopper.geometry import xyz_to_point
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _wind_tunnel:
    if area_of_interest_:
        raise NotImplementedError(
          '\nArea of interest is not implemented yet!\nThis component uses '
          'geometry bounding box as the area of interest.\n'
          'You can use offset inputs to adjust the current bounding box.'
        )
    grad_xyz, cell_count = _wind_tunnel.calculate_grading(
        _cell_size_[0], _cell_to_cell_ratio_[0], wake_offset_, height_offset_)
    cell_count_xyz = xyz_to_point(cell_count)
    cell_count_tot = int(cell_count_xyz.X * cell_count_xyz.Y * cell_count_xyz.Z)
