# assign inputs
_xGrading_, _yGrading_, _zGrading_ = IN
gradXYZ = None

try:
    from butterfly.grading import SimpleGrading
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

gradXYZ = SimpleGrading(_xGrading_, _yGrading_, _zGrading_)


# assign outputs to OUT
OUT = (gradXYZ,)