# assign inputs
_turbulenceProp_, _temperature_, fvSchemes_, fvSolution_, residualControl_, _relaxationFactors_ = IN
recipe = None

try:
    from butterfly.recipe import HeatTransfer
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _temperature_:
    _temperature_ += 273.15

recipe = HeatTransfer(_turbulenceProp_, fvSchemes_, fvSolution_, residualControl_,
                      _relaxationFactors_, TRef=_temperature_)

l = len(recipe.quantities)
q = ''.join(q + ' ..... ' if (c + 1) % 4 != 0 and c + 1 != l else q + '\n'
            for c, q in enumerate(recipe.quantities))


# assign outputs to OUT
OUT = (recipe,)