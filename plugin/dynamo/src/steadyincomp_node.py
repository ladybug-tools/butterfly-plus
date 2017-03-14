# assign inputs
_turbulenceProp_, fvSchemes_, fvSolution_, residualControl_, _relaxationFactors_ = IN
recipe = None

try:
    from butterfly.recipe import SteadyIncompressible
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

recipe = SteadyIncompressible(_turbulenceProp_, fvSchemes_, fvSolution_,
                              residualControl_, _relaxationFactors_)

l = len(recipe.quantities)
q = ''.join(q + ' ..... ' if (c + 1) % 4 != 0 and c + 1 != l else q + '\n'
            for c, q in enumerate(recipe.quantities))



# assign outputs to OUT
OUT = (recipe,)