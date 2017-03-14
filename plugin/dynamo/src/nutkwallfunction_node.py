# assign inputs
_value, _Cmu_, _kappa_, _E_ = IN
nutkWallFunction = None

try:
    from butterfly.fields import NutkWallFunction
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _value:
    nutkWallFunction = NutkWallFunction(_value, _Cmu_, _kappa_, _E_)


# assign outputs to OUT
OUT = (nutkWallFunction,)