# assign inputs
_funcObject = IN[0]
funcObject = None

try:
    from butterfly.functions import Function
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _funcObject:
    funcObject = Function.fromCppDictionary(_funcObject)


# assign outputs to OUT
OUT = (funcObject,)