from taipy.gui import State, notify
import aisuite as ai
from google import genai
import os

def init_llm(state: State):
    llm_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    return llm_client

#TODO: Use context here
def request(state: State, prompt: str) -> str:
    # response = state.client.chat.completions.create(
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": f"{prompt}",
    #         }
    #     ],
    #     model="gpt-4-turbo-preview",
    # )
    # return response.choices[0].message.content
    response = state.llm_client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    return response.text