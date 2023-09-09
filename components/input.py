import dash_bootstrap_components as dbc
from dash import html, dcc


def render_chat_input():
    chat_input = html.Div(
        [
            html.Div(
                dcc.Input(
                    id="user-input",
                    placeholder="Send a message",
                    type="text",
                    className="chat-input",
                ),
                className="input-wrapper",
            ),
            html.Button(id="submit", value="Send", className="chat-send-btn"),
        ],
        className="chat-input-wrapper",
    )

    return chat_input
