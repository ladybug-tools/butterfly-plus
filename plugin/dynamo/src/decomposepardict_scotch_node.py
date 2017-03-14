# assign inputs
_numOfCpus_ = IN[0]
decomposeParDict = None

try:
    from butterfly.decomposeParDict import DecomposeParDict
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))


try:
    numberOfSubdomains = int(_numOfCpus_)
except:
    numberOfSubdomains = 2

decomposeParDict = DecomposeParDict.scotch(numberOfSubdomains)


# assign outputs to OUT
OUT = (decomposeParDict,)