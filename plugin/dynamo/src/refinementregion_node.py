# assign inputs
_name, _geo, _refMode, _meshSet_ = IN
refinementRegion = None

try:
    from butterfly_dynamo.refinementRegion import RefinementRegionDS
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _geo and _name and _refMode:
    refinementRegion = RefinementRegionDS(_name, _geo, _refMode, _meshSet_)


# assign outputs to OUT
OUT = (refinementRegion,)