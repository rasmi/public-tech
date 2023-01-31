"""Expense model."""

from dataclasses import dataclass
from enum import Enum
from enum import auto

from common import Frequency


class ExpenseType(Enum):
    "Expense types."""
    CHILD_CARE = auto()
    CHILD_SUPPORT = auto()
    DEPENDENT_CARE = auto()
    RENT = auto()
    MEDICAL = auto()
    HEATING = auto()
    COOLING = auto()
    MORTGAGE = auto()
    UTILITIES = auto()
    TELEPHONE = auto()
    INSURANCE_PREMIUMS = auto()


@dataclass
class Expense:
    """Expense model."""
    expense_type: ExpenseType
    frequency: Frequency
    amount: float
