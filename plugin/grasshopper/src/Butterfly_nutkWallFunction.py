# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
nutk Wall Function boundary condition.

-
    Args:
        _value: input value.
        _Cmu_: model coefficient.
        _kappa_: Von Karman constant.
        _E_: model coefficient.
    Returns:
        nutk_wall_funct: nutk Wall Function boundary condition.
"""

ghenv.Component.Name = "Butterfly_nutkWallFunction"
ghenv.Component.NickName = "nutkWallFunction"
ghenv.Component.Message = 'VER 0.0.05\nJAN_12_2019'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "02::BoundaryCondition"
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from butterfly.fields import NutkWallFunction
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _value:
    nutk_wall_funct = NutkWallFunction(_value, _Cmu_, _kappa_, _E_)
