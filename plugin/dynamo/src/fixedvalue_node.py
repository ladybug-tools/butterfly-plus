# assign inputs
_value = IN[0]
fixedValue = None

try:
    from butterfly.fields import FixedValue
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _value:
    fixedValue = FixedValue(_value)


# assign outputs to OUT
OUT = (fixedValue,)