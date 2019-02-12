# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Butterfly; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Wind vector.

-

    Args:
        _wind_speed: Wind speed in m/s at a the reference height (_refWindHeight_).
        _wind_direction_: Wind direction as Vector3D (default: 0, 1, 0).
    Returns:
        wind_vector: Wind Vector.
"""

ghenv.Component.Name = "Butterfly_Wind Vector"
ghenv.Component.NickName = "WindVector"
ghenv.Component.Message = 'VER 0.0.05\nJAN_12_2019'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "00::Create"
ghenv.Component.AdditionalHelpFromDocStrings = "3"

if _wind_speed and _wind_direction_:
    try:
        _wind_direction_.Unitize()
        wind_vector = _wind_speed * _wind_direction_
    except AttributeError:
        # dynamo
        nv = _wind_direction_.Normalized();
        wind_vector = nv.Scale(_wind_speed);