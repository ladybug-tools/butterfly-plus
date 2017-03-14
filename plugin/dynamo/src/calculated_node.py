# assign inputs

calculated = None

try:
    from butterfly.fields import Calculated
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

calculated = Calculated()


# assign outputs to OUT
OUT = (calculated,)