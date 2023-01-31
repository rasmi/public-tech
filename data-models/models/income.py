"""Income model."""

from dataclasses import dataclass
from enum import Enum
from enum import auto

from common import Frequency


class IncomeType(Enum):
    """Income types."""
    WAGES = auto()
    SELF_EMPLOYMENT = auto()
    UNEMPLOYMENT = auto()
    CASH_ASSISTANCE = auto()
    CHILD_SUPPORT = auto()
    DISABILITY_MEDICAID = auto()
    SSI = auto()
    SS_DEPENDENT = auto()
    SS_DISABILITY = auto()
    SS_SURVIVOR = auto()
    SS_REITREMENT = auto()
    NYS_DISABILITY = auto()
    VETERAN = auto()
    PENSION = auto()
    DEFERRED_COMP = auto()
    WORKERS_COMP = auto()
    ALIMONY = auto()
    BOARDER = auto()
    GIFTS = auto()
    RENTAL = auto()
    INVESTMENT = auto()


@dataclass
class Income:
    """Income model."""
    income_type: IncomeType
    frequency: Frequency
    amount: float
