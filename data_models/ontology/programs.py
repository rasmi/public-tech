"""Program definitions."""
from typing import Dict

from .models import Program
from .models import Information
from .models import Document
from .program_requirements import snap
from .program_requirements import childcare


class SNAP(Program):
    """SNAP program."""

    requirements: Dict[Information, list[Document]] = snap.requirements


class ChildCare(Program):
    """Child Care Assistance program."""

    requirements: Dict[Information, list[Document]] = childcare.requirements
