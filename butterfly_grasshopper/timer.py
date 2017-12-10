# coding=utf-8
"""Grasshopper timer."""
try:
    import Grasshopper as gh
except ImportError:
    pass


def gh_component_timer(gh_comp, interval=600, pause=False):
    """
    Update the component at the interval like using a GH timer.

    Modified from ShapeOpGHPython.
    Github: github.com/AndersDeleuran/ShapeOpGHPython
    Authors: Anders Holden Deleuran (CITA/KADK), Mario Deuss (LGG/EPFL)

    Args:
        gh_comp: Grasshopper component.
        interval: Interval in milliseconds (default: 600).
        pause: Pause timer if set to True
    """
    # return if pause
    if pause:
        return

    # Ensure interval is larger than zero
    interval = max((1, interval))

    # Get the Grasshopper document and component that owns this script
    gh_doc = gh_comp.OnPingDocument()

    # Define the callback function
    def call_back(gh_doc):
        gh_comp.ExpireSolution(False)

    # Update the solution
    gh_doc.ScheduleSolution(interval,
                            gh.Kernel.GH_Document.GH_ScheduleDelegate(call_back))
