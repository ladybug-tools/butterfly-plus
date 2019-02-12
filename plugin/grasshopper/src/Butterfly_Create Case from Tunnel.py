# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Create Case from wind tunnel.

-

    Args:
        _name: Project name.
        _BF_geo: List of butterfly geometries that will be inside the tunnel.
        ref_regions_: A list of refinement regions.
        _wind_vector: A vector that indicates speed and direction of wind. Length
            of the vector will be used as windspeed and the unfied vector will be
            used for wind direction. For wind tunnel vector will be projected to
            XY plane.
        _ref_wind_height_: Reference height for wind velocity (default: 10m).
        _landscape_: An integer between 0-7 to calculate z0 (roughness).
            You can find full description of the landscape in Table I at this
            link (onlinelibrary.wiley.com/doi/10.1002/met.273/pdf)

            0 > '0.0002'  # sea. Open sea or lake (irrespective of wave size),
            tidal flat, snow-covered flat plain, featureless desert, tarmac and
            concrete, with a free fetch of several kilometres

            1 > '0.005'   # smooth. Featureless land surface without any noticeable
            obstacles and with negligible vegetation; e.g. beaches, pack ice without
            large ridges, marsh and snow-covered or fallow open country.

            2 > '0.03'    # open. Level country with low vegetation (e.g. grass)
            and isolated obstacles with separations of at least 50 obstacle heights;
            e.g. grazing land without wind breaks, heather, moor and tundra,
            runway area of airports. Ice with ridges across-wind.

            3 > '0.10'    # roughly open. Cultivated or natural area with low crops
            or plant covers, or moderately open country with occasional obstacles
            (e.g. low hedges, isolated low buildings or trees) at relative horizontal
            distances of at least 20 obstacle heights

            4 > '0.25'    # rough. Cultivated or natural area with high crops or
            crops of varying height, and scattered obstacles at relative distances
            of 12-15 obstacle heights for porous objects (e.g. shelterbelts) or
            8-12 obstacle heights for low solid objects (e.g. buildings).

            5 > '0.5'     # very rough. Intensively cultivated landscape with many
            rather large obstacle groups (large farms, clumps of forest) separated
            by open spaces of about eight obstacle heights. Low densely planted
            major vegetation like bush land, orchards, young forest. Also, area
            moderately covered by low buildings with interspaces of three to
            seven building heights and no high trees.

            6 > '1.0'     # Skimming. Landscape regularly covered with similar-size
            large obstacles, with open spaces of the same order of magnitude as
            obstacle heights; e.g. mature regular forests, densely built-up area
            without much building height variation.

            7 > '2.0'     # chaotic. City centres with mixture of low-rise and
            high-rise buildings, or large forests of irregular height with many
            clearings.
        make_2d_params_: Butterfly parameters to make a 2d wind tunnel.
        _tunnel_params_: Butterfly tunnel parameters.
        _run: Create wind tunnel case from inputs.
    Returns:
        report: Reports, errors, warnings, etc.
        block_pts: Points showing the corners of the wind tunnel (for visualization).
        wind_tunnel: Butterfly wind tunnel.
        case: Butterfly case.
"""

ghenv.Component.Name = "Butterfly_Create Case from Tunnel"
ghenv.Component.NickName = "createCaseFromTunnel"
ghenv.Component.Message = 'VER 0.0.05\nJAN_12_2019'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "00::Create"
ghenv.Component.AdditionalHelpFromDocStrings = "3"


try:
    from butterfly_grasshopper.windtunnel import WindTunnelGH
    from butterfly_grasshopper.geometry import xyz_to_point
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))


def main():
    # meshing parameters are moved to blockMesh and snappyHexMesh components
    _meshParams_ = None
    
    wt = WindTunnelGH.from_geometries_wind_vector_and_parameters(
        _name, _BF_geo, _wind_vector, _tunnel_params_, _landscape_,
        _meshParams_, _ref_wind_height_)
        
    for region in ref_regions_:
        wt.add_refinementRegion(region)
    
    # save with overwrite set to False. User can clean the folder using purge if they need to.
    case = wt.save(overwrite=(_run + 1) % 2, make2d_parameters=make_2d_params_)
    
    print "Wind tunnel dimensions: {}, {} and {}".format(
        case.blockMeshDict.width, case.blockMeshDict.length, case.blockMeshDict.height)
    
    pts = (xyz_to_point(v) for v in case.blockMeshDict.vertices)

    return wt, pts, case

if _run and _name and _BF_geo and _wind_vector:
        wind_tunnel, block_pts, case = main()

