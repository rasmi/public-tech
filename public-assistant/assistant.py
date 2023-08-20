"""A helpful public assistant."""
import program_data
import service_guide
import simpleaichat


if __name__ == "__main__":
    import dotenv

    dotenv.load_dotenv()

    program_list = program_data.load_program_data().to_json(orient="records")
    service_guide_prompt = service_guide.ServiceGuidePrompt(program_list)

    guide = simpleaichat.AIChat(model="gpt-4", system=service_guide_prompt.content)
    response = guide(
        "I am a single mother of two and I just lost my job.",
        output_schema=service_guide.RelevantPrograms,
    )
    print(response)
