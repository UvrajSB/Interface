from taipy.gui import State, notify
import aisuite as ai
from google import genai
import os, sys
import Anonymisation.anonymisation as anon
import logging

logging.basicConfig(
    level=logging.DEBUG,  # Set to DEBUG to capture all messages
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)  # Print logs to the terminal
    ]
)

logger = logging.getLogger(__name__)

def init_llm(state: State):
    llm_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    return llm_client

def request(state: State, prompt: str) -> str:
    response = state.llm_client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    return response.text

def anonymised_request(state: State, prompt: str) -> str:
    logger.debug(f"The prompt is:\n {prompt}")
    anonymised_result, entity_mapping = anon.anonymize_prompt(prompt)
    prompt = anonymised_result.text
    logger.debug(f"The anonymised prompt is:\n {prompt}")
    response = state.llm_client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    logger.debug(f"The response is:\n {response.text}")
    response = anon.deanonymize_response(response.text, entity_mapping)
    logger.debug(f"The deanonymised response is:\n {response}")
    return response