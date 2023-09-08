from dash import html
import dash_bootstrap_components as dbc
from app import app


def render_textbox(text: str, box: str = "AI"):
    text = text.replace(f"ChatBot:", "").replace("Human:", "")

    if box == "human":
        textbox_human = dbc.Card(
            text, body=True, style={"color": "gray"}, color="#ffffff", inverse=False
        )

        return html.Div(
            [textbox_human],
            style={
                "display": "flex",
                "margin-bottom": "0.5rem",
                "flex-direction": "row-reverse",
            },
        )
    elif box == "AI":
        thumbnail = html.Img(
            src=app.get_asset_url("chatbot.png"),
            style={
                "border-radius": 50,
                "height": 36,
                "margin-right": 5,
                "float": "left",
            },
        )

        textbox = dbc.Card(
            text, style={"color": "#99b0d9"}, body=True, color="#345ba0", inverse=False
        )

        return html.Div(
            [thumbnail, textbox],
            style={
                "display": "flex",
                "margin-bottom": "0.5rem",
                "flex-direction": "row",
            },
        )

    else:
        raise ValueError("Incorrect option for `box`.")
