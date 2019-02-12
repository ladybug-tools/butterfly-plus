# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Generate fvSchemes based on mesh non-orthogonalities.

-
    Args:
        _quality: Solution quality [0..1]. The quality 0 generates div_schemes
            which is less accurate but more stable. The quality 1 generates a
            div_schemes that are more accurate but less stable. You can start with
            quality 0 and then change it to quality 1 when the solution is
            converging.
    Returns:
        readMe!: Reports, errors, warnings, etc.
        div_schemes: Recommended div schemes. Use solution parameter to update
            fvSchemes for the solution.
"""

ghenv.Component.Name = "Butterfly_divSchemes library"
ghenv.Component.NickName = "genDivSchemes"
ghenv.Component.Message = 'VER 0.0.05\nJAN_12_2019'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "08::Etc"
ghenv.Component.AdditionalHelpFromDocStrings = "3"

try:
    from butterfly.fvSchemes import FvSchemes
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _quality is not None:
    div_schemes = FvSchemes.divSchemesCollector[_quality%2]

