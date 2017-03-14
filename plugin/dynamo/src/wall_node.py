# assign inputs
temperature_ = IN[0]
wallBoundary = None

try:
    from butterfly.boundarycondition import IndoorWallBoundaryCondition
    from butterfly.fields import FixedValue
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

temperature_ = FixedValue(str(temperature_ + 273.15)) \
               if temperature_ \
               else None

wallBoundary = IndoorWallBoundaryCondition(T=temperature_)



# assign outputs to OUT
OUT = (wallBoundary,)