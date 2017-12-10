# coding=utf-8
"""Unit conversion to meters for Grasshopper."""
try:
    import scriptcontext as sc
    import Rhino.UnitSystem as us
except ImportError:
    pass


def convert_document_units_to_meters():
    """Calculate converToMeters value for this document."""
    doc_unit = sc.doc.ModelUnitSystem

    if doc_unit == us.Meters:
        return 1.0000
    elif doc_unit == us.Centimeters:
        return 0.010
    elif doc_unit == us.Millimeters:
        return 0.0010
    elif doc_unit == us.Feet:
        return 0.3050
    elif doc_unit == us.Inches:
        return 0.0254
    elif doc_unit == us.Kilometers:
        return 1000.0000
    else:
        print "Unknown unit. Meters will be used instead."
        return 1.0000
