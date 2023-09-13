import openai
import os

from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from components.textbox import render_textbox

from app import app
from dotenv import load_dotenv

load_dotenv()

TOKEN_LIMIT = int(os.getenv("TOKEN_LIMIT"))

message_history = []


@app.callback(
    Output(component_id="display-conversation", component_property="children"),
    Input(component_id="store-conversation", component_property="data"),
)
def update_display(data):
    if not data:
        # Initial bot's reply to "hello" when the page loads
        message_history.append({"role": "user", "content": "hello"})
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k", messages=message_history, max_tokens=TOKEN_LIMIT
        )
        reply_content = completion.choices[0]["message"].content
        message_history.append({"role": "assistant", "content": reply_content})
        return [render_textbox(reply_content, "AI")]

    display_messages = []
    for msg in message_history[2:]:
        role = "AI" if msg["role"] == "assistant" else "human"
        display_messages.append(render_textbox(msg["content"], role))

    return display_messages


@app.callback(
    Output(component_id="user_input", component_property="value"),
    Input(component_id="submit", component_property="n_clicks"),
    Input(component_id="user-input", component_property="n_submit"),
)
def clear_input(n_clicks, n_submit):
    return ""


@app.callback(
    Output(component_id="store-conversation", component_property="data"),
    Output(component_id="loading-component", component_property="children"),
    Output(component_id="user-input", component_property="value"),
    Input(component_id="submit", component_property="n_clicks"),
    Input(component_id="user-input", component_property="n_submit"),
    State(component_id="user-input", component_property="value"),
    State(component_id="store-conversation", component_property="data"),
)
def run_chatbot(n_clicks, n_submit, user_input, chat_history):
    if n_clicks == 0 and n_submit is None:
        return "", None, user_input

    if user_input is None or user_input == "":
        return chat_history, None, user_input

    message_history.append({"role": "user", "content": user_input})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k", messages=message_history, max_tokens=TOKEN_LIMIT
    )

    reply_content = completion.choices[0]["message"].content
    message_history.append({"role": "assistant", "content": reply_content})

    return message_history, None, ""
