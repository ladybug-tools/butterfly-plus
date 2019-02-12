# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Update fvSchemes values based on mesh orthogonalities.

-

    Args:
        _BF_objs: A list of butterfly objects.
        colors_: Optional input for colors to 
    Returns:
        report: Reports, errors, warnings, etc.
        geometries: List of geometries as meshes.
"""

ghenv.Component.Name = "Butterfly_Get Geometry"
ghenv.Component.NickName = "getGeometry"
ghenv.Component.Message = 'VER 0.0.05\nJAN_12_2019'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "08::Etc"
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from butterfly_grasshopper.geometry import bf_mesh_to_mesh
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))
else:
    from itertools import chain

def get_geometry(obj):
    """Get Grasshopper geometry from butterfly objects."""
    try:
        return obj.geometry
    except AttributeError:
        try:
            return obj.geometries
        except AttributeError:
            print '{} has no geometry!'.format(type(obj))

if _BF_objs:
    geo = chain.from_iterable(get_geometry(obj) for obj in _BF_objs)
    
    try:
        geo = tuple(geo)
    except TypeError:
        pass
    else:
        if not colors_:
            col = [None] * len(geo)
        else:
            l = len(colors_)
            col = (colors_[c % l] for c, g in enumerate(geo))

        geometries = (bf_mesh_to_mesh(g, c) for g, c in zip(geo, col))

