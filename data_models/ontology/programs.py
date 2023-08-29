"""Program definitions."""

from .program_requirements import snap
from .program_requirements import childcare


class Program:
    """Representation of a program and its information requirements."""

    requirements = {}


class SNAP(Program):
    """SNAP program."""

    requirements = snap.requirements


class ChildCare(Program):
    """Child Care Assistance program."""

    requirements = childcare.requirements
