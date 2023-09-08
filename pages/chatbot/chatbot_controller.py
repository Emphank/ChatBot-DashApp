import openai

from dash.dependencies import Input, Output, State
from app import app

from components.textbox import render_textbox
from pages.chatbot.chatbot_model import converstaion


message_history = []


@app.callback(
    Output(component_id="display-conversation", component_property="children"),
    Input(component_id="store-conversation", component_property="data"),
)
def update_display(data):
    if not data:
        return []
    return [
        render_textbox(
            message_history[i]["content"], box="human" if i % 2 == 0 else "AI"
        )
        for i in range(len(message_history))
    ]


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
    Input(component_id="submit", component_property="n_clicks"),
    Input(component_id="user-input", component_property="n_submit"),
    State(component_id="user-input", component_property="value"),
    State(component_id="store-conversation", component_property="data"),
)
def run_chatbot(n_clicks, n_submit, user_input, chat_history):
    print(user_input)
    if n_clicks == 0 and n_submit is None:
        return "", None

    if user_input is None or user_input == "":
        return chat_history, None

    message_history.append({"role": "user", "content": user_input})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=message_history
    )

    reply_content = completion.choices[0]["message"].content
    message_history.append({"role": "assistant", "content": reply_content})

    # chat_history += f"Human: {user_input}<split>ChatBot: "
    # result_ai = converstaion.predict(input=user_input)
    # model_output = result_ai.strip()
    # chat_history += f"{model_output}<split>"
    # user_input = ""
    return message_history, None
