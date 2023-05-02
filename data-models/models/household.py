"""Household model."""

from dataclasses import dataclass


@dataclass
class Household:
    """Information related to a household."""

    # pylint: disable=too-many-instance-attributes

    city: str
    zip: str

    members: int

    assets: int

    living_renting: bool
    living_owner: bool
    living_staying_with_friend: bool
    living_hotel: bool
    living_shelter: bool
    living_prefer_not_to_say: bool

    living_rental_type: str
