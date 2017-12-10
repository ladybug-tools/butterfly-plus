# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Function Object.

    Args:
        _funcObject: An OpenFOAM function object in (c++) dictionary format.
    Returns:
        funcObject: A function object.
"""
ghenv.Component.Name = "Butterfly_Function Object"
ghenv.Component.NickName = "functionObject"
ghenv.Component.Message = 'VER 0.0.04\nNOV_22_2017'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "06::Solution"
ghenv.Component.AdditionalHelpFromDocStrings = "2"

try:
    from butterfly.functions import Function
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _funcObject:
    funcObject = Function.from_cpp_dictionary(_funcObject)
