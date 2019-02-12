# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Load probes from a folder.

-

    Args:
        _solution: Butterfly Solution, Case or fullpath to the case folder.
        _field: Probes' filed as a string (e.g. p, U).
        
    Returns:
        probes: List of probes as points.
"""

ghenv.Component.Name = "Butterfly_Load Probes"
ghenv.Component.NickName = "loadProbes"
ghenv.Component.Message = 'VER 0.0.05\nJAN_12_2019'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "07::PostProcess"
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from butterfly.utilities import load_probes_from_postProcessing_file
    from butterfly_grasshopper.geometry import xyz_to_point
    import butterfly_grasshopper.unitconversion as uc
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

import os


if _solution and _field:
    if isinstance(_solution, str):
        project_dir = _solution.replace('\\\\','/').replace('\\','/')
        probes_dir = os.path.join(project_dir, 'postProcessing\\probes') 
        raw_values = load_probes_from_postProcessing_file(probes_dir, _field)
    else:
        assert hasattr(_solution, 'loadProbes'), \
            'Invalid Input: <{}> is not a valid Butterfly Solution.'.format(_solution)
        try:
            raw_values = _solution.load_probes(_field)
        except Exception as e:
            raise ValueError('Failed to load probes:\n\t{}'.format(e))
    
    c = 1.0 / uc.convert_document_units_to_meters()
    try:
        probes = tuple(xyz_to_point(v, c) for v in raw_values)
    except:
        probes = raw_values
