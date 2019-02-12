# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Set parameters for snappyHexMeshDict.
Read more about snappyHexMeshDict here:
    https://openfoamwiki.net/images/f/f0/Final-AndrewJacksonSlidesOFW7.pdf


    Args:
        _mesh_quality_: Use 0-2 to auto generate the parameters for meshQualityControls
        _castellated_mesh_: Set to True to castellated mesh (default: True).
        _snap_: Set to True to snap mesh to the surfaces (default: True).
        _add_layers_: Set to True to push mesh away from surfaces and add layers (default: False).
        _n_cells_btwn_levels_: Number of cells between levels.
        _max_global_cells_: An intger for the maximum number of global cells (default: 2000000).
        _srf_feature_level_: An integer for the extract features refinement. Default is None which
            means implicit meshing feature will be used.
        _expansion_ratio_: Layers expansion ration (default: 1.1)
        _final_layer_thickness_: Thickness of final layer (default: 0.7)
        _min_thickness_: Minimum thickness for layers (default: 0.1).
        _n_layer_iter_: Overall max number of layer addition iterations. The mesher
            will exit if it reaches this number of iterations; possibly with an
            illegal mesh (default: 50).
        additional_par_: Additional parameters as a valid c++ dictionary. Additional values
            will overwrite the values from the other inputs above.
    Returns:
        snappy_hex_mesh_dict: Butterfly snappyHexMeshDict.
"""

ghenv.Component.Name = "Butterfly_snappyHexMeshDict"
ghenv.Component.NickName = "snappyHexMeshDict"
ghenv.Component.Message = 'VER 0.0.05\nJAN_12_2019'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "03::Mesh"
ghenv.Component.AdditionalHelpFromDocStrings = "2"

try:
    from butterfly.solution import SolutionParameter
    from butterfly.parser import CppDictParser
    from butterfly.utilities import update_dict
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _mesh_quality_:
    raise NotImplementedError('MeshQuality is not implemented yet. It will be added soon.')

values = {'castellatedMesh': str(_castellated_mesh_).lower(),
          'snap': str(_snap_).lower(), 'addLayers': str(_add_layers_).lower(),
          'castellatedMeshControls': {
            'nCellsBetweenLevels': str(_n_cells_btwn_levels_),
            'maxGlobalCells': str(_max_global_cells_)
            },
           'addLayersControls': {
                'expansionRatio': str(_expansion_ratio_),
                'finalLayerThickness': str(_final_layer_thickness_),
                'minThickness': str(_min_thickness_),
                'nLayerIter': str(_n_layer_iter_)}
          }

if _srf_feature_level_ is not None:
    values['snapControls'] = {'extractFeaturesRefineLevel': str(_srf_feature_level_)}

if additional_par_:
    try:
        addedValues = CppDictParser(additional_par_).values
    except Exception as e:
        raise ValueError("Failed to load additional_par_:\n%s" % str(e))
    else:
        values = update_dict(values, addedValues)

snappy_hex_mesh_dict = SolutionParameter('snappyHexMeshDict', values)

