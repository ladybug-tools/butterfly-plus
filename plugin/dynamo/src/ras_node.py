# assign inputs
_RASModel_, _turbulence_, _printCoeffs_ = IN
RAS = None

try:
    from butterfly.turbulenceProperties import TurbulenceProperties
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))


RAS = TurbulenceProperties.RAS(_RASModel_, _turbulence_, _printCoeffs_)


# assign outputs to OUT
OUT = (RAS,)