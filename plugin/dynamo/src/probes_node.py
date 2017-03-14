# assign inputs
_points, _fields_, _writeInterval_ = IN
probes = None

try:
    from butterfly.functions import Probes
    import butterfly_dynamo.unitconversion as uc
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _points:
    probes = Probes()
    c = uc.convertDocumentUnitsToMeters()
    probes.probeLocations = ((p.X * c, p.Y * c, p.Z * c) for p in _points)
    probes.fields = _fields_
    probes.writeInterval = _writeInterval_


# assign outputs to OUT
OUT = (probes,)