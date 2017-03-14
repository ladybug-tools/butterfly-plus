# assign inputs
_pressure_, temperature_ = IN
outletBoundary = None

try:
    from butterfly.boundarycondition import FixedOutletBoundaryCondition
    from butterfly.fields import FixedValue
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

_pressure_ = FixedValue(_pressure_) if _pressure_ else None

temperature_ = FixedValue(str(temperature_ + 273.15)) if temperature_ \
               else None

outletBoundary = FixedOutletBoundaryCondition(p=_pressure_, T=temperature_)



# assign outputs to OUT
OUT = (outletBoundary,)