# assign inputs
_quantities, _values_ = IN
residualControl = None

try:
    from butterfly.fvSolution import ResidualControl
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _quantities:
    if not _values_:
        _values_ = (0.0001,)
    
    # match length
    l = len(_quantities)
    values = (_values_[c] if c < len(_values_) else _values_[-1]
        for c, q in enumerate(_quantities))

    residualControl = ResidualControl(
        {key: value for (key, value) in zip(_quantities, values)}
    )



# assign outputs to OUT
OUT = (residualControl,)