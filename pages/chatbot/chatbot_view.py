import json
import openai
import os

import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

# import components
from components.navbar import render_navbar
from components.input import render_chat_input

import pages.chatbot.chatbot_controller as chatbot_controller
from dotenv import load_dotenv

load_dotenv()

# define layout
chatbot_layout = html.Div(
    id="display-conversation",
    className="chat-wrapper",
)


def render_chatbot():
    with open("././context.json", "r") as file:
        context_data = json.load(file)
        context = context_data["context"]
        chatbot_controller.message_history.clear()

        chatbot_controller.message_history.append(
            {"role": "system", "content": context}
        )

        # chatbot_controller.message_history.append({"role": "user", "content": "hello"})

        # completion = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo", messages=chatbot_controller.message_history
        # )

        # reply_content = completion.choices[0]["message"].content
        # chatbot_controller.message_history.append(
        #     {"role": "assistant", "content": reply_content}
        # )

    return html.Div(
        [
            html.Br(),
            dcc.Store(id="store-conversation", data=""),
            dbc.Container(
                fluid=True,
                children=[
                    dbc.Row(
                        [
                            dbc.Col(
                                width=10,
                                children=html.Div(
                                    [
                                        chatbot_layout,
                                        render_chat_input(),
                                        dbc.Spinner(html.Div(id="loading-component")),
                                    ],
                                    style={
                                        "border-radius": 25,
                                        "background": "#12172d",
                                        "display": "flex",
                                        "flex-direction": "column",
                                        "justify-content": "space-between",
                                        "height": "97.5vh",
                                    },
                                ),
                            ),
                        ],
                        style={
                            "display": "flex",
                            "justify-content": "center",
                        },
                    )
                ],
            ),
        ],
        style={"background": "#060415"},
    )
