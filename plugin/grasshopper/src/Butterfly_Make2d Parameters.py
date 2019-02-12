# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Make a case 2d.


    Args:
        _origin: Origin point for the 2d case cutting plane.
        _normal: Normal direction for the cutting plane as a vector.
        _width_: Width of 2d case (default: 0.5)
    Returns:
        report: Reports, errors, warnings, etc.
        make_2d_params: Parameters for creating a 2d case.
"""

ghenv.Component.Name = "Butterfly_Make2d Parameters"
ghenv.Component.NickName = "make2dParams"
ghenv.Component.Message = 'VER 0.0.05\nJAN_12_2019'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "00::Create"
ghenv.Component.AdditionalHelpFromDocStrings = "4"

try:
    from butterfly.make2dparameters import Make2dParameters
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

# create blockMeshDict based on BBox
if _origin and _normal:
    try:
        make_2d_params = Make2dParameters(_origin, _normal, _width_)
    except TypeError:
        # DynamoBIM
        make_2d_params = Make2dParameters(
            (_origin.X, _origin.Y, _origin.Z),
            (_normal.X, _normal.Y, _normal.Z),
            _width_)


