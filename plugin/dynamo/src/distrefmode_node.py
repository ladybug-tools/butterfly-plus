# assign inputs
_levels_0, _levels_1 = IN
distanceRefMode = None

try:
    from butterfly.refinementRegion import Distance
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

_level = [tuple(i) for i in [_levels_0, _levels_1] if i]

if _level:
    distanceRefMode = Distance(_level)


# assign outputs to OUT
OUT = (distanceRefMode,)