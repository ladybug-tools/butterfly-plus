# assign inputs
_origin, _normal, _width_ = IN
make2dParams = None

try:
    from butterfly.make2dparameters import Make2dParameters
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

# create blockMeshDict based on BBox
if _origin and _normal:
    try:
        make2dParams = Make2dParameters(_origin, _normal, _width_)
    except TypeError:
        # DynamoBIM
        make2dParams = Make2dParameters(
            (_origin.X, _origin.Y, _origin.Z),
            (_normal.X, _normal.Y, _normal.Z),
            _width_)




# assign outputs to OUT
OUT = (make2dParams,)