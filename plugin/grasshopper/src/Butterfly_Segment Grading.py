# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Segment Grading.
Use this component to create a grading for a segment of the block based on ratio
or length.

-

    Args:
        _percentage_length: Percentage of length of the block.
        _percentage_cells: Percentage of cells to be included in this segment.
        _expansion_ratio_: Expansion ration in this segment (default: 1).
        
    Returns:
        segment_grading: A segment grading. Use MultiGrading component to create
            a grading.
"""

ghenv.Component.Name = "Butterfly_Segment Grading"
ghenv.Component.NickName = "segGrading"
ghenv.Component.Message = 'VER 0.0.05\nJAN_12_2019'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "03::Mesh"
ghenv.Component.AdditionalHelpFromDocStrings = "3"

try:
    from butterfly.grading import Grading
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _percentage_length and _percentage_cells:
    segment_grading = Grading(_percentage_length, _percentage_cells, _expansion_ratio_)
