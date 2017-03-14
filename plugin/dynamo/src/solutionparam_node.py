# assign inputs
_filename, _values, tRange_, replace_ = IN
solutionParam = None

try:
    from butterfly.solution import SolutionParameter
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _filename and _values:
    solutionParam = SolutionParameter.fromCppDictionary(_filename, _values,
                                                     replace_, tRange_)


# assign outputs to OUT
OUT = (solutionParam,)