# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Inside/Ouside region refinement.

-

    Args:
        _mode_: Refinement mode (0: inside, 1: outside).
        _level: Refinement level as an integer. All cells inside the surface get
            refined up to the level. The surface needs to be closed for this to
            be possible.
    Returns:
        location_ref_mode: Refinement mode.
"""

ghenv.Component.Name = "Butterfly_LocationRefinementMode"
ghenv.Component.NickName = "inOUTRefMode"
ghenv.Component.Message = 'VER 0.0.05\nJAN_12_2019'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "00::Create"
ghenv.Component.AdditionalHelpFromDocStrings = "5"

try:
    from butterfly.refinementRegion import Inside, Outside
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _level:
    if not _mode_:
        location_ref_mode = Inside(_level)
    else:
        location_ref_mode = Outside(_level)
