# coding=utf-8
"""Unit conversion to meters for Dynamo."""
try:
    import clr
    clr.AddReference('RevitAPI')
    clr.AddReference('RevitServices')
    from RevitServices.Persistence import DocumentManager
    from Autodesk.Revit.DB import UnitType, DisplayUnitType
except ImportError:
    pass


def convert_document_units_to_meters():
    """Calculate converToMeters value for this document."""
    doc = DocumentManager.Instance.CurrentDBDocument
    docunits = doc.GetUnits()
    doc_unit = docunits.GetFormatOptions(UnitType.UT_Length).DisplayUnits

    if doc_unit == DisplayUnitType.DUT_METERS:
        return 1.0000
    elif doc_unit == DisplayUnitType.DUT_CENTIMETERS:
        return 0.010
    elif doc_unit == DisplayUnitType.DUT_MILLIMETERS:
        return 0.0010
    elif doc_unit == DisplayUnitType.DUT_DECIMAL_FEET:
        return 0.3050
    elif doc_unit == DisplayUnitType.DUT_FEET_FRACTIONAL_INCHES:
        return 0.3050
    elif doc_unit == DisplayUnitType.DUT_FRACTIONAL_INCHES:
        return 0.0254
    elif doc_unit == DisplayUnitType.DUT_DECIMAL_INCHES:
        return 0.0254
    else:
        print("Unknown unit. Meters will be used instead.")
        return 1.0000
