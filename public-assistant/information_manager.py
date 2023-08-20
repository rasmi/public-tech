"""Information manager that keeps track of information requirements for each program."""
from pydantic import BaseModel
from pydantic import Field


class InformationManagerPrompt:
    """Prompt template for an Information Manager."""

    role: str = "system"

    template: str = """
    You are a public assistant gathering information necessary for me to submit an application to access a benefit.
    The table below includes pieces of information necessary for this benefit application, as well as which documents are necessary to prove that information.
    Working one item at a time, ask me for the relevant documentation for each piece of information until all requirements are satisfied.
    Do your best to minimize the amount of documentation I need to provide by asking for documentation that can satisfy multiple requirements.
    Also choose documentation that would be relatively simple to access.
    At each step, explain which information requirements have been satisfied and which still need documentation, as well as suggestions for what documentation can satisfy these requirements. 

    The information requirements table is here:
    {information_requirements_details}
    """
    content: str

    def __init__(self, information_requirements_details) -> None:
        self.content = self.template.format(
            information_requirements_details=information_requirements_details
        )


class InformationRequirement(BaseModel):
    """A piece of required information and its relevant documentation."""

    information: str = Field(description="Information required.")
    provided_documentation: str = Field(
        description="Documentation provided to meet the requirement."
    )


class InformationCollection(BaseModel):
    """A collection of information requirements to be satisfied."""

    information_gathered: list[InformationRequirement] = Field(
        description="A collection of information requirements already satisfied."
    )
    information_still_needed: list[InformationRequirement] = Field(
        description="A collection of information requirements that still need to be satisfied."
    )