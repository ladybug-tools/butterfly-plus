# assign inputs
_cellSizeXYZ_, _gradXYZ_, _locationInMesh_, _globRefineLevel_ = IN
meshParams = None

try:
    # import butterfly
    from butterfly.meshingparameters import MeshingParameters
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

# create blockMeshDict based on BBox
if _cellSizeXYZ_:
    _cellSizeXYZ_ = _cellSizeXYZ_.X, _cellSizeXYZ_.Y, _cellSizeXYZ_.Z

meshParams = MeshingParameters(
    _cellSizeXYZ_, _gradXYZ_, _locationInMesh_, _globRefineLevel_)


# assign outputs to OUT
OUT = (meshParams,)