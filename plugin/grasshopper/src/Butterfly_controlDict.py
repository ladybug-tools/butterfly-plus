# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Set parameters for runDict

    Args:
        _start_time_: Start timestep (default: 0)
        _end_time_: End timestep (default: 1000)
        _write_interval_: Number of intervals between writing the results (default: 100)
        _write_compression_: Set to True if you want the results to be compressed
            before being written to your machine (default: False).
        _purge_write_: Number of results folder to be kept. 0 means that all the
            result folder will be kept (default: 0).
        func_objects_: A list of OpenFOAM function objects. Use functionObject
            component to create a butterfly function object from a cpp dictionary.
    Returns:
        control_dict: Butterfly control dictionary.
"""
ghenv.Component.Name = "Butterfly_controlDict"
ghenv.Component.NickName = "controlDict"
ghenv.Component.Message = 'VER 0.0.05\nJAN_12_2019'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "06::Solution"
ghenv.Component.AdditionalHelpFromDocStrings = "2"

try:
    from butterfly.controlDict import ControlDict
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))


cd = ControlDict()
if _start_time_ is not None:
    cd.startTime = _start_time_

if _end_time_ is not None:
    cd.endTime = _end_time_

if _write_interval_ is not None:
    cd.writeInterval = _write_interval_

if _write_compression_ is not None:
    cd.writeCompression = _write_compression_

if _purge_write_ is not None:
    cd.purgeWrite = _purge_write_

if func_objects_ and func_objects_[0] is not None:
    cd.functions = func_objects_

control_dict = cd
