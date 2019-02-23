# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Run recipes using OpenFOAM.

-

    Args:
        _case: A Butterfly case.
        _recipe: A Butterfly recipe.
        decompose_par_dict_: decomposeParDict for parallel run. By default solution
            runs in serial.
        solution_par_: Butterfly solutionParams. These parameters can be edited
            while the analysis is running. Ensure to use valid values. Butterfly
            does not check the input values for accuracy.
        _interval_: Time interval for updating solution in Grasshopper in seconds.
            (default: 2 seconds)
        _write_: Write changes to folder.
        _run: start running the solution.
    Returns:
        report: Reports, errors, warnings, etc.
        is_running: Boolean to note whether the simulation is running.
        timestep: Iteration count of the simulation.
        residual_fields: The names of the residual fields.
        residual_values: The values for each of the residual fields noted above.
        log_files: File path to the log file for the simulation
"""

ghenv.Component.Name = "Butterfly_Solution"
ghenv.Component.NickName = "solution"
ghenv.Component.Message = 'VER 0.0.05\nFEB_22_2019'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "06::Solution"
ghenv.Component.AdditionalHelpFromDocStrings = "1"

from scriptcontext import sticky
import os

try:
    from butterfly_grasshopper.timer import gh_component_timer
    from butterfly.solution import Solution
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

uniqueKey = str(ghenv.Component.InstanceGuid)

if not _interval_:
    _interval_ = 2

if _case and _recipe and _write: 
    try:
        if uniqueKey not in sticky:
            # solution hasn't been created or has been removed
            # create a new one and copy it to sticky
            solution = Solution(_case, _recipe, decompose_par_dict_, solution_par_)
            residual_fields = solution.residual_fields
            # pass solution parameter to __init__
            sticky[uniqueKey] = solution
            if run_:
                timestep = solution.timestep
                solution.update_solution_params(solution_par_, timestep)
                if _interval_ < 0:
                    # wait for the run to be done
                    solution.run(wait=True)
                else:
                    solution.run(wait=False)
        else:
            # solution is there so just load it
            solution = sticky[uniqueKey]
            residual_fields = solution.residual_fields
    
        is_running = solution.is_running
        info = solution.info
        timestep = info.timestep
        residual_values = info.residualValues
        if run_ and is_running:
            print 'running...'
            # update parameters if there has been changes.
            solution.update_from_recipe(_recipe)
            solution.update_solution_params(solution_par_, timestep)
            gh_component_timer(ghenv.Component, interval=_interval_*1000)
        else:
            # analysis is over
            solution = sticky[uniqueKey]
            if run_:
                solution.terminate()
            # remove solution from sticky
            if uniqueKey in sticky:
                del(sticky[uniqueKey])
            
            print 'done!'
            
            # set run toggle to False
        
        ghenv.Component.Message = "\nTime = {}".format(timestep)
        
    except Exception as e:
        # clean up solution in case of failure
        if solution and run_:
            solution.terminate()
        if uniqueKey in sticky:
            del(sticky[uniqueKey])
        
        print '***\n{}\n***'.format(e)
        import traceback
        print(traceback.format_exc())
    if solution:
        log_files = solution.log_files or os.path.join(_case.project_dir,
                                                       _recipe.log_file)