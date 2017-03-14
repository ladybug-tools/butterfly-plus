# assign inputs
_segmentGradings = IN[0]
grading = None

try:
    from butterfly.grading import MultiGrading
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _segmentGradings:
    grading = MultiGrading(_segmentGradings)


# assign outputs to OUT
OUT = (grading,)