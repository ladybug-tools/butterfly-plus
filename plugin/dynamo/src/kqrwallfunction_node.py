# assign inputs
_value = IN[0]
kqRWallFunction = None


try:
    from butterfly.fields import KqRWallFunction
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))    

if _value:
    kqRWallFunction = KqRWallFunction(_value)


# assign outputs to OUT
OUT = (kqRWallFunction,)