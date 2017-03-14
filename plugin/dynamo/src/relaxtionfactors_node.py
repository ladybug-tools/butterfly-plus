# assign inputs
_quantities, _values = IN
relaxationFactors = None

try:
    from butterfly.fvSolution import RelaxationFactors
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))


if _quantities and _values:
    
    assert len(_quantities) == len(_values), \
        'Length of quantities [%d] must be equal to the length of values [%d].' \
        % (len(_quantities), len(_values))

    relaxationFactors = RelaxationFactors(
        {key: value for (key, value) in zip(_quantities, _values)}
    )


# assign outputs to OUT
OUT = (relaxationFactors,)