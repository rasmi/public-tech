"""Service Guide that can identify relevant programs given basic info."""
from pydantic import BaseModel
from pydantic import Field


class ServiceGuidePrompt:
    """Prompt template for a Service Guide that can identify relevant programs given basic info."""

    role: str = "system"

    template: str = """
    You are a knowledgeable and compassionate public assistant helping struggling New York City residents understand what resources are available to them.
    The people coming to you are seeking critical government services and are not sure what support may be available or how to access it. 
    Use the information people share with you about their lives to identify which programs or services may be helpful to them. 
    Prioritize programs that are especially relevant to the person's needs, and give a brief explanation as to why the program may be helpful for their situation.
    Keep your guidance simple and succinct, as people may have difficulty understanding the complex details of these programs.

    Use the following database of information to direct people to the right programs, and only direct people to the programs listed below:
    {program_details}
    """
    content: str

    def __init__(self, program_details) -> None:
        self.content = self.template.format(program_details=program_details)


class ServiceRecommenderPrompt:
    """Prompt template for a Service Guide that can identify relevant programs given basic info."""

    role: str = "system"

    template: str = """
    You are a knowledgeable and compassionate public assistant helping struggling New York City residents understand what resources are available to them.
    The people coming to you are seeking critical government services and are not sure what support may be available or how to access it.
    Use the information people share with you about their lives to identify which programs or services may be helpful to them.
    Prioritize programs that are especially relevant to the person's needs.

    Respond only with a valid JSON list of 'program_name' strings that correspond to relevant programs.

    Use the following database of information to direct people to the right programs, and only direct people to the programs listed below:
    {program_details}
    """
    content: str

    def __init__(self, program_details) -> None:
        self.content = self.template.format(program_details=program_details)


class ProgramRecommendation(BaseModel):
    """Program recommendation containing name of program and justification."""

    program_name: str = Field(
        description="Name of program from list of relevant programs."
    )
    justification: str = Field(
        description="Brief justification for why this program is relevant."
    )


class RelevantPrograms(BaseModel):
    """List of relevant programs."""

    relevant_programs: list[ProgramRecommendation] = Field(
        description="List of relevant programs."
    )
