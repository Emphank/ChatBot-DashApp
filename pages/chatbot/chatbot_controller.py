import openai

from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from components.textbox import render_textbox

from app import app


message_history = []


@app.callback(
    Output(component_id="display-conversation", component_property="children"),
    Input(component_id="store-conversation", component_property="data"),
)
def update_display(data):
    if not data:
        return []

    message_boxes = []
    for i in range(1, len(message_history)):
        if i % 2 == 0:
            message_boxes.append(render_textbox(message_history[i]["content"], "AI"))
        else:
            message_boxes.append(render_textbox(message_history[i]["content"], "human"))

    return message_boxes


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
        model="gpt-3.5-turbo", messages=message_history
    )

    reply_content = completion.choices[0]["message"].content
    message_history.append({"role": "assistant", "content": reply_content})

    return message_history, None, ""
