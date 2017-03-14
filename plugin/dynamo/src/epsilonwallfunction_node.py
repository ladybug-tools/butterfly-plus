# assign inputs
_value, _Cmu_, _kappa_, _E_ = IN
epsilonWallFunction = None

try:
    from butterfly.fields import EpsilonWallFunction
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _value:
    epsilonWallFunction = EpsilonWallFunction(_value, _Cmu_, _kappa_, _E_)



# assign outputs to OUT
OUT = (epsilonWallFunction,)