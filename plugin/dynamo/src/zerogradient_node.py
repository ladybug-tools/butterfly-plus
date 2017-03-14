# assign inputs

zeroGradient = None

try:
    from butterfly.fields import ZeroGradient
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

zeroGradient = ZeroGradient()



# assign outputs to OUT
OUT = (zeroGradient,)