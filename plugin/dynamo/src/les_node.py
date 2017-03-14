# assign inputs
_LESModel_, _delta_, _turbulence_, _printCoeffs_ = IN
LES = None

try:
    from butterfly.turbulenceProperties import TurbulenceProperties
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))


LES = TurbulenceProperties.LES(_LESModel_, _delta_, _turbulence_, _printCoeffs_)


# assign outputs to OUT
OUT = (LES,)