# assign inputs
_startTime_, _endTime_, _writeInterval_, _writeCompression_, _purgeWrite_, funcObjects_ = IN
controlDict = None

try:
    from butterfly.controlDict import ControlDict
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))


cd = ControlDict()
if _startTime_ is not None:
    cd.startTime = _startTime_

if _endTime_ is not None:
    cd.endTime = _endTime_

if _writeInterval_ is not None:
    cd.writeInterval = _writeInterval_

if _writeCompression_ is not None:
    cd.writeCompression = _writeCompression_

if _purgeWrite_ is not None:
    cd.purgeWrite = _purgeWrite_

if funcObjects_ and funcObjects_[0] is not None:
    cd.functions = funcObjects_

controlDict = cd


# assign outputs to OUT
OUT = (controlDict,)