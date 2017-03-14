# assign inputs
_name, _geo, _boundary_, refineLevels_, nSrfLayers_, _meshSet_ = IN
BFGeometries = None

try:
    from butterfly_dynamo.geometry import BFGeometryDS
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _geo and _name:
    BFGeometries = BFGeometryDS(_name, _geo, _boundary_, refineLevels_, nSrfLayers_, _meshSet_)


# assign outputs to OUT
OUT = (BFGeometries,)