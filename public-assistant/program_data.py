"""Load and process data about public assistance programs in NYC."""

import pandas as pd
import pydantic
import html2text

BENEFITS_DATA_URL = "https://data.cityofnewyork.us/api/views/kvhd-5fmu/rows.csv"

CORE_PROGRAMS = [
    "Cash Assistance",
    "Supplemental Nutrition Assistance Program",
    "Special Supplemental Nutrition Program for Women, Infants, and Children",
    "Emergency Rental Assistance Program",
    "Emergency Assistance / One Shot Deal",
    "Child Care Vouchers",
    "Disability Rent Increase Exemption",
    "Senior Citizen Rent Increase Exemption",
    "Family Homelessness and Eviction Prevention Supplement",
    "NYS Paid Family Leave",
    "NYC Care",
    "Medicaid for Pregnant Women",
]


class ProgramInfo(pydantic.BaseModel):
    """A public assistance program in New York City."""

    program_name: str
    program_acronym: str
    program_category: str
    population_served: list[str]
    program_description: str
    plain_language_eligibility: str
    required_documents_summary: str


def load_program_data() -> pd.DataFrame:
    """Load and process data about public assistance programs in NYC.

    Only keep a certain subset of columns that will be most helpful in prompts.
    Re-format HTML to plain text.

    Returns:
        A dataframe with information about public assistance programs.
    """
    benefits = pd.read_csv(BENEFITS_DATA_URL)

    html_columns = [
        "program_description",
        "plain_language_eligibility",
        "required_documents_summary",
    ]

    core_benefits = benefits[benefits["program_name"].isin(CORE_PROGRAMS)]
    core_benefits = core_benefits[ProgramInfo.__fields__.keys()]
    core_benefits["population_served"] = core_benefits["population_served"].apply(
        lambda x: x.split(",")
    )

    html_formatter = html2text.HTML2Text()
    html_formatter.ignore_links = True
    html_formatter.single_line_break = True
    core_benefits[html_columns] = core_benefits[html_columns].applymap(
        html_formatter.handle, na_action="ignore"
    )

    core_benefits = core_benefits.fillna("")

    return core_benefits
