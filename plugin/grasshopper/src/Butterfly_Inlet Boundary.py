# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Create an inlet boundary with uniform velocity value.

-

    Args:
        _velocity_vec: Velocity vector.
        temperature_: Temperature in degrees celsius.
    Returns:
        inlet_boundary: Buttefly inlet boundary.
"""

ghenv.Component.Name = "Butterfly_Inlet Boundary"
ghenv.Component.NickName = "inletvel"
ghenv.Component.Message = 'VER 0.0.05\nJAN_12_2019'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "01::Boundary"
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from butterfly import boundarycondition as bc
    from butterfly.fields import FixedValue
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _velocity_vec:
    _velocity_vec = FixedValue(str((_velocity_vec.X, _velocity_vec.Y, _velocity_vec.Z)).replace(',', '')) \
                   if _velocity_vec \
                   else None

    temperature_ = FixedValue(str(temperature_ + 273.15)) \
                   if temperature_ \
                   else None
                   
    inlet_boundary = bc.FixedInletBoundaryCondition(U=_velocity_vec,
                                                    T = temperature_)

