# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Scotch decomposeParDict. Dictionary for parallel runs.

-

    Args:
        _numOfCpus_: Number of cpus (default: 2).
    Returns:
        decomposeParDict: decomposeParDict.
"""

ghenv.Component.Name = "Butterfly_decomposeParDict scotch"
ghenv.Component.NickName = "decomposeParDict_scotch"
ghenv.Component.Message = 'VER 0.0.04\nMAR_14_2017'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "08::Etc"
ghenv.Component.AdditionalHelpFromDocStrings = "2"

try:
    from butterfly.decomposeParDict import DecomposeParDict
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))


try:
    numberOfSubdomains = int(_numOfCpus_)
except:
    numberOfSubdomains = 2

decomposeParDict = DecomposeParDict.scotch(numberOfSubdomains)
