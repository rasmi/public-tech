"""A helpful public assistant."""
import program_data
import service_guide
import information_requirements
import information_manager

import simpleaichat


def run_service_guide():
    """Example run of the service guide."""
    program_list = program_data.load_program_data().to_json(orient="records")
    service_guide_prompt = service_guide.ServiceGuidePrompt(program_list)

    guide = simpleaichat.AIChat(model="gpt-4", system=service_guide_prompt.content)
    response = guide(
        "I am a single mother of two and I just lost my job.",
        output_schema=service_guide.RelevantPrograms,
    )
    print(response)


def run_information_manager():
    """Example run of the information manager."""
    snap_requirements = information_requirements.load_snap_detailed()
    information_manager_prompt = information_manager.InformationManagerPrompt(
        information_requirements_details=snap_requirements
    )

    info_manager = simpleaichat.AIChat(
        model="gpt-4", system=information_manager_prompt.content
    )
    response = info_manager(
        "Here is my driver's license.",
        output_schema=information_manager.InformationCollection,
    )
    print(response)
    # Parse response back into Pydantic models.
    # Note: Parsing back into specific Document subclasses is not yet supported.
    # See https://github.com/pydantic/pydantic/discussions/7008
    parsed_response = information_manager.InformationCollection.model_validate(response)
    print(parsed_response)


if __name__ == "__main__":
    import dotenv

    dotenv.load_dotenv()
