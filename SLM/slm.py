from taipy.gui import State, notify
from langchain_ollama import ChatOllama, chat_models
import ollama
from bs4 import BeautifulSoup

def init_slm(state: State):
    selected_slm = "deepseek-r1:1.5b"
    model_names = {model['model'] for model in ollama.list()["models"]}
    if selected_slm in model_names:
        notify(state, "success", f"{selected_slm} is available")
    else:
        notify(state, "error", f"{selected_slm} is not available.")
    slm_client = ChatOllama(model="deepseek-r1:1.5b")
    return slm_client
        
#TODO: Use context here
def request(state: State ,prompt: str) -> str:
    response = state.slm_client.invoke(prompt).content
    soup = BeautifulSoup(response, "html.parser")
    formatted_response = soup.get_text(separator="\n")
    return formatted_response