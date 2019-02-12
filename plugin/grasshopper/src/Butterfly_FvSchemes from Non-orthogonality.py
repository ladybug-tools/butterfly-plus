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
        _non_orthogonality: Maximum mesh non-orthogonality as an integer.
    Returns:
        report: Reports, errors, warnings, etc.
        fv_schemes: Recommended fvSchemes. Use solution parameter to update fvSchemes
            for the solution.
"""

ghenv.Component.Name = "Butterfly_FvSchemes from Non-orthogonality"
ghenv.Component.NickName = "genFvSchemes"
ghenv.Component.Message = 'VER 0.0.05\nJAN_12_2019'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "08::Etc"
ghenv.Component.AdditionalHelpFromDocStrings = "3"

try:
    from butterfly.fvSchemes import FvSchemes
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if  _non_orthogonality:
    fv_schemes = FvSchemes.from_mesh_orthogonality(_non_orthogonality)

