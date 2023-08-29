"""Program definitions."""
from .models import Program
from .program_requirements import snap
from .program_requirements import childcare


class SNAP(Program):
    """SNAP program."""

    requirements = snap.requirements


class ChildCare(Program):
    """Child Care Assistance program."""

    requirements = childcare.requirements
