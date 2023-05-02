"""Person model."""

from dataclasses import dataclass
from enum import Enum
from enum import auto

from expense import Expense
from income import Income


class HeadOfHouseholdRelation(Enum):
    """Relationship of person to the head of household."""

    CHILD = auto()
    FOSTER_CHILD = auto()
    STEP_CHILD = auto()
    GRANDCHILD = auto()
    SPOUSE = auto()
    PARENT = auto()
    FOSTER_PARENT = auto()
    STEP_PARENT = auto()
    GRANDPARENT = auto()
    SISTER_BROTHER = auto()
    STEP_SISTER_STEP_BROTHER = auto()
    BOYFRIEND_GIRLFRIEND = auto()
    DOMESTIC_PARTNER = auto()
    UNRELATED = auto()
    RELATED_IN_SOME_OTHER_WAY = auto()


@dataclass
class Person:
    """Information related to a person."""

    # pylint: disable=too-many-instance-attributes

    age: int

    head_of_household: bool
    head_of_household_relation: HeadOfHouseholdRelation

    student: bool
    student_full_time: bool

    pregnant: bool

    unemployed: bool
    unemployed_worked_last_18_months: bool

    blind: bool
    disabled: bool
    veteran: bool

    benefits_medicaid: bool
    benefits_medicaid_disability: bool

    income: list[Income]
    expenses: list[Expense]

    living_owner_on_deed: bool
    living_rental_on_lease: bool
