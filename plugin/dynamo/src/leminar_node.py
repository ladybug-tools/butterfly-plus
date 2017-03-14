# assign inputs

laminar = None

try:
    from butterfly.turbulenceProperties import TurbulenceProperties
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))


laminar = TurbulenceProperties.laminar()


# assign outputs to OUT
OUT = (laminar,)