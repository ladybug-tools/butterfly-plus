# assign inputs
_percentageLength, _percentageCells, _expansionRatio_ = IN
segmentGrading = None

try:
    from butterfly.grading import Grading
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _percentageLength and _percentageCells:
    segmentGrading = Grading(_percentageLength, _percentageCells, _expansionRatio_)


# assign outputs to OUT
OUT = (segmentGrading,)