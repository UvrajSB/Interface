import os
import sys
from taipy.gui import Gui, State, notify
import aisuite as ai
import GUI.gui as gui
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

client = None
context = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today? "
conversation = {
    "Conversation": []
}
current_user_message = ""
past_conversations = []
selected_conv = None
selected_row = [1]
value = ["Cloud LLM", "On-Device LLM", "Auto Prompt Routing"]
content = "/GUI/logo.png"

def on_init(state: State) -> None:
    state.context = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today? "
    state.conversation = {
        "Conversation": []
    }
    state.current_user_message = ""
    state.past_conversations = []
    state.selected_conv = None
    state.selected_row = [1]


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
    
    #Offline response
    #response = chat_model.invoke(prompt).content

    messages = [
        {"role": "system", "content": "Respond in Pirate English."},
        {"role": "user", "content": "Tell me a joke."},
    ]
    
    message = {
        "role": "user",
        "content": prompt,
    }
    
    model = "google:"

    response = client.chat.completions.create(
        model=model,
        message=message,
        temperature=0.75
    )
    return response.choices[0].message.content

def update_context(state: State) -> None:
    state.context += f"Human: \n {state.current_user_message}\n\n AI:"
    answer = request(state, state.context)
    state.context += answer
    state.selected_row = [len(state.conversation["Conversation"]) + 1]
    return answer


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


def reset_chat(state: State) -> None:
    state.past_conversations = state.past_conversations + [
        [len(state.past_conversations), state.conversation]
    ]
    state.conversation = {
        "Conversation": [""]
    }


def tree_adapter(item: list) -> [str, str]:
    identifier = item[0]
    if len(item[1]["Conversation"]) > 3:
        return (identifier, item[1]["Conversation"][2][:50] + "...")
    return (item[0], "Empty conversation")

past_prompts = []

if __name__ == "__main__":
    load_dotenv()

    #client = openai.Client(api_key=os.getenv("OPENAI_API_KEY"))
    LLM_client = ai.Client()
    #local inferencing
    #chat_model = ChatOllama(model="deepseek-r1:1.5b")
    Gui(gui.page).run(debug=True, use_reloader=True ,title="Interface")
