# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Solution Parameters.

    Args:
        control_dict_: controlDict.
        residualControl_: residualControl.
        probes_: probes.
        additional_par_: List of solution parameters. Use solutionParameter
            component to create solution_par.
    Returns:
        solution_par: A list of solution parameters.
"""
ghenv.Component.Name = "Butterfly_Solution Parameters"
ghenv.Component.NickName = "solutionParams"
ghenv.Component.Message = 'VER 0.0.05\nJAN_12_2019'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "06::Solution"
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
     from butterfly.solution import SolutionParameter
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if control_dict_:
    control_dict_ = SolutionParameter.from_cpp_dictionary('controlDict', str(control_dict_))

if probes_:
    probes_ = SolutionParameter.from_cpp_dictionary('probes', str(probes_))


params = [control_dict_, probes_] + additional_par_

solution_par = (p for p in params if p)

