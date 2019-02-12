# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Create Butterfly surface.

-

    Args:
        _geo: Grasshopper geometries.
        _name: Geometry name.
        _boundary_: Boundary for this surface (e.g. Inlet, Outlet, Wall)
        refine_levels_: Geometry refinement level as a tuple of two intger (min, max).
        n_srf_layers_: Number of layers for snappyHexMesh.
        _mesh_set_: Grasshopper mesh settings.
    Returns:
        report: Reports, errors, warnings, etc.
        BF_geo: A Buttefly geometry.
"""

ghenv.Component.Name = "Butterfly_Create Butterfly Geometry"
ghenv.Component.NickName = "createBFGeometry"
ghenv.Component.Message = 'VER 0.0.05\nJAN_12_2019'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "00::Create"
ghenv.Component.AdditionalHelpFromDocStrings = "2"

try:
    from butterfly_grasshopper.geometry import BFGeometryGH
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _geo and _name:
    BF_geo = BFGeometryGH(_name, _geo, _boundary_, refine_levels_, n_srf_layers_, _mesh_set_)
