# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Create a custom boundary.

-

    Args:
        _b_type_: Boundary type (e.g wall, patch, etc.)
        _U_: Boundary condition for U (velocity).
        _p_: Boundary condition for P (pressure).
        _p_rgh_: Boundary condition for P_rgh.
        _k_: Boundary condition for k.
        _epsilon: Boundary condition for epsilon.
        _nut_: Boundary condition for nut.
        _T_: Boundary condition for T (temperature).
    Returns:
        report: Reports, errors, warnings, etc.
        boundary: Buttefly custom boundary.
"""

ghenv.Component.Name = "Butterfly_Boundary"
ghenv.Component.NickName = "boundary"
ghenv.Component.Message = 'VER 0.0.05\nJAN_12_2019'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "01::Boundary"
ghenv.Component.AdditionalHelpFromDocStrings = "2"

try:
    from butterfly import boundarycondition
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

_b_type_ = 'patch' if not _b_type_ else _b_type_

boundary = boundarycondition.BoundaryCondition(
    _b_type_, U=_U_, p=_p_, k=_k_, epsilon=_epsilon_,
    nut=_nut_, alphat=_alphat_, p_rgh=_p_rgh_, T=_T_
)

boundary = boundary.duplicate()
