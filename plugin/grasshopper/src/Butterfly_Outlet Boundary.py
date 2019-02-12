# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Create an outlet boundary with uniform pressure value.

-

    Args:
        _pressure_: Pressure as a float (default: 0).
        temperature_: Temperature in degrees celsius.
    Returns:
        outlet_boundary: Buttefly outlet boundary.
"""

ghenv.Component.Name = "Butterfly_Outlet Boundary"
ghenv.Component.NickName = "outlet"
ghenv.Component.Message = 'VER 0.0.05\nJAN_12_2019'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "01::Boundary"
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from butterfly.boundarycondition import FixedOutletBoundaryCondition
    from butterfly.fields import FixedValue
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

_pressure_ = FixedValue(_pressure_) if _pressure_ else None

temperature_ = FixedValue(str(temperature_ + 273.15)) if temperature_ \
               else None

outlet_boundary = FixedOutletBoundaryCondition(p=_pressure_, T=temperature_)

