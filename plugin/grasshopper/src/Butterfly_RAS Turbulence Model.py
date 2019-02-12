# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Reynolds-averaged simulation (RAS) turbulence model.

Read more: http://cfd.direct/openfoam/user-guide/turbulence/
Watch this: https://www.youtube.com/watch?v=Eu_4ppppQmw

    Args:
        _RAS_model_: Name of RAS turbulence model (default: RNGkEpsilon).
            Incompressible RAS turbulence models:
                LRR, LamBremhorstKE, LaunderSharmaKE, LienCubicKE,
                LienLeschziner, RNGkEpsilon, SSG, ShihQuadraticKE,
                SpalartAllmaras, kEpsilon, kOmega, kOmegaSSTSAS, kkLOmega,
                qZeta, realizableKE, v2f
            Compressible RAS turbulence models:
                LRR, LaunderSharmaKE, RNGkEpsilon, SSG, SpalartAllmaras,
                buoyantKEpsilon, kEpsilon, kOmega, kOmegaSSTSAS,
                realizableKE, v2f
        _turbulence_: Boolean switch to turn the solving of turbulence
            modelling on/off (default: True).
        _print_coeffs_: Boolean switch to print model coeffs to terminal at
            simulation start up (default: True).
    
    Returns:
        RAS: Reynolds-averaged simulation (RAS) turbulence model.
"""

ghenv.Component.Name = "Butterfly_RAS Turbulence Model"
ghenv.Component.NickName = "RAS"
ghenv.Component.Message = 'VER 0.0.05\nJAN_12_2019'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "04::Turbulence"
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from butterfly.turbulenceProperties import TurbulenceProperties
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))


RAS = TurbulenceProperties.RAS(_RAS_model_, _turbulence_, _print_coeffs_)
