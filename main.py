import os
import sys
from taipy.gui import Gui, State, notify

import logging

import GUI.gui as gui
from dotenv import load_dotenv
import LLM.llm as llm
import SLM.slm as slm

logging.basicConfig(
    level=logging.DEBUG,  # Set to DEBUG to capture all messages
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)  # Print logs to the terminal
    ]
)

logger = logging.getLogger(__name__)


client = None
context = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today? "
conversation = {
    "Conversation": []
}
current_user_message = ""
past_conversations = []
selected_conv = None
selected_row = [1]
content = "/GUI/logo.png"
current_mode = "Cloud LLM"
llm_client = None
slm_client = None

def on_init(state: State) -> None:
    state.context = context
    state.conversation = conversation
    state.current_user_message = current_user_message
    state.past_conversations = past_conversations
    state.selected_conv = selected_conv
    state.selected_row = selected_row
    state.current_mode = current_mode
    
    state.llm_client = llm.init_llm(state)
    state.slm_client = slm.init_slm(state)
    logger.debug(type(llm_client))
    logger.debug(type(slm_client))

def update_context(state: State) -> None:
    state.context += f"Human: \n {state.current_user_message}\n\n AI:"
    answer=""
    logger.debug(state.current_mode)
    match state.current_mode:
        case "Cloud LLM":
            answer = llm.request(state, state.context)
        case "Secure Cloud LLM":
            answer = llm.request(state, state.context)
        case "On-Device LLM":
            logger.info("Reached inside On-Device LLM")
            logger.info(type(slm_client))
            answer = slm.request(state, state.context)
        case "Auto Prompt Routing":
            answer = llm.request(state, state.context)
    state.context += answer
    state.selected_row = [len(state.conversation["Conversation"]) + 1]
    return answer

    #cannot access local variable 'answer' where it is not associated with a value

def reset_chat(state: State) -> None:
    state.past_conversations = state.past_conversations + [
        [len(state.past_conversations), state.conversation]
    ]
    state.conversation = {
        "Conversation": [""]
    }
    
def send_message(state: State) -> None:
    notify(state, "info", "Sending message...")
    answer = update_context(state)
    conv = state.conversation._dict.copy()
    conv["Conversation"] += [state.current_user_message, answer]
    state.current_user_message = ""
    state.conversation = conv
    notify(state, "success", "Response received!")


def style_conv(state: State, idx: int, row: int) -> str:
    if idx is None:
        return None
    elif idx % 2 == 0:
        return "user_message"
    else:
        return "gpt_message"


def on_exception(state, function_name: str, ex: Exception) -> None:
    notify(state, "error", f"An error occured in {function_name}: {ex}")

def tree_adapter(item: list) -> [str, str]:
    identifier = item[0]
    if len(item[1]["Conversation"]) > 3:
        return (identifier, item[1]["Conversation"][2][:50] + "...")
    return (item[0], "Empty conversation")

past_prompts = []

if __name__ == "__main__":
    load_dotenv()
    Gui(gui.page).run(debug=True, use_reloader=True ,title="Interface")

