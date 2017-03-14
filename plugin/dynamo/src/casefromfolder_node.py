# assign inputs
name_, _folder, _run = IN
case = None

try:
    from butterfly_dynamo.case import Case
    import butterfly_dynamo.unitconversion as uc
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _folder and _run: 
    # create OpenFoam Case
    case = Case.fromFolder(_folder, name_, 1.0 / uc.convertDocumentUnitsToMeters())
    case.save(overwrite=False)


# assign outputs to OUT
OUT = (case,)