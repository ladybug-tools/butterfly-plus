# assign inputs
_windwardX_, _topX_, _sidesX_, _leewardX_ = IN
tunnelParams = None

try:
    from butterfly.windtunnel import TunnelParameters
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

tunnelParams = TunnelParameters(_windwardX_, _topX_, _sidesX_, _leewardX_)


# assign outputs to OUT
OUT = (tunnelParams,)