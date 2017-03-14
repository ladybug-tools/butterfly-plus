# assign inputs
_nonOrthogonality = IN[0]
fvSchemes = None

try:
    from butterfly.fvSchemes import FvSchemes
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if  _nonOrthogonality:
    fvSchemes = FvSchemes.fromMeshOrthogonality(_nonOrthogonality)



# assign outputs to OUT
OUT = (fvSchemes,)