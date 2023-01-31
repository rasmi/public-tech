"""Common models."""
from enum import Enum
from enum import auto


class Frequency(Enum):
    """Frequency of income or expense types."""
    WEEKLY = auto()
    BIWEEKLY = auto()
    MONTHLY = auto()
    SEMIMONTHLY = auto()
    YEARLY = auto()
