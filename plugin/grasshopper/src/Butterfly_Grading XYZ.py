# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Grading XYZ
Create a grading for different XYZ.

-

    Args:
        _x_grading_: X grading.
        _y_grading_: Y grading.
        _z_grading_: Z grading.
        
    Returns:
        grad_xyz: A butterfly Grading. Connect this output to blockMesh component
            to set grading of blockMesh in X, Y or Z direction.
"""

ghenv.Component.Name = "Butterfly_Grading XYZ"
ghenv.Component.NickName = "gradXYZ"
ghenv.Component.Message = 'VER 0.0.05\nJAN_12_2019'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "03::Mesh"
ghenv.Component.AdditionalHelpFromDocStrings = "3"

try:
    from butterfly.grading import SimpleGrading
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

grad_xyz = SimpleGrading(_x_grading_, _y_grading_, _z_grading_)
