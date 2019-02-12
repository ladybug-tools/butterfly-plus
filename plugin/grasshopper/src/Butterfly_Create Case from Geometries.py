# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Create an OpenFOAM Case from geometries.

-

    Args:
        _name: Project name.
        _BF_geo: List of butterfly geometries for this case.
        ref_regions_: A list of refinement regions.
        make_2d_params_: Butterfly parameters to make a 2d wind tunnel.
        expand_block_mesh_: Butterfly by default expands the mesh by one cell to
            ensure snappyHexMesh will snap to extrior surfaces. You can set the
            expand to off or overwrite the vertices using update blockMeshDict
            component.
        _run: Create case from inputs.
    Returns:
        report: Reports, errors, warnings, etc.
        block_pts: Points showing the corners of the wind tunnel (for visualization).
        case: Butterfly case.
"""

ghenv.Component.Name = "Butterfly_Create Case from Geometries"
ghenv.Component.NickName = "caseFromGeos"
ghenv.Component.Message = 'VER 0.0.05\nJAN_12_2019'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "00::Create"
ghenv.Component.AdditionalHelpFromDocStrings = "2"

try:
    from butterfly_grasshopper.case import Case
    from butterfly_grasshopper.geometry import xyz_to_point
    import butterfly_grasshopper.unitconversion as uc
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _run and _name and _BF_geo:
    # meshing parameters are moved to blockMesh and snappyHexMesh components
    _mesh_params_ = None
    
    # create OpenFoam Case
    ctm = uc.convert_document_units_to_meters()
    
    case = Case.from_bf_geometries(_name, tuple(_BF_geo),
        meshing_parameters=_mesh_params_, make2d_parameters=make_2d_params_,
        convertToMeters=ctm)
    
    for reg in ref_regions_:
        case.add_refinement_region(reg)
    
    if expand_block_mesh_:
        xCount, yCount, zCount = 1, 1, 1
        if case.blockMeshDict.is2d_in_x_direction:
            xCount = 0
        if case.blockMeshDict.is2d_in_y_direction:
            yCount = 0
        if case.blockMeshDict.is2d_in_z_direction:
            zCount = 0
        
        case.blockMeshDict.expand_by_cells_count(xCount, yCount, zCount)
    
    block_pts = (xyz_to_point(v) for v in case.blockMeshDict.vertices)
    
    case.save(overwrite=(_run + 1) % 2)

