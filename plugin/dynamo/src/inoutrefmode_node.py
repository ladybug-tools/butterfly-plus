# assign inputs
_mode_, _level = IN
locationRefMode = None

try:
    from butterfly.refinementRegion import Inside, Outside
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _level:
    if not _mode_:
        locationRefMode = Inside(_level)
    else:
        locationRefMode = Outside(_level)


# assign outputs to OUT
OUT = (locationRefMode,)