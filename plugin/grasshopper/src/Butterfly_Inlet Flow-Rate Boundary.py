# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Create an inlet boundary with flow rate in m3/s.

-

    Args:
        _vol_flow_rate: Volumetric flow rate in m3/s.
        temperature_: Temperature in degrees celsius.
    Returns:
        inlet_boundary: Buttefly inlet boundary.
"""

ghenv.Component.Name = "Butterfly_Inlet Flow-Rate Boundary"
ghenv.Component.NickName = "inletVol"
ghenv.Component.Message = 'VER 0.0.05\nJAN_12_2019'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "01::Boundary"
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from butterfly import boundarycondition as bc
    from butterfly.fields import FixedValue, FlowRateInletVelocity
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _vol_flow_rate:
    
    velocity =  FlowRateInletVelocity(_vol_flow_rate, '(0 0 0)')
    
    temperature_ = FixedValue(str(temperature_ + 273.15)) \
                   if temperature_ \
                   else None
                   
    inlet_boundary = bc.FixedInletBoundaryCondition(U=velocity, T = temperature_)

