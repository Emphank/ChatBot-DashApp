from dash import html
import dash_bootstrap_components as dbc


def render_textbox(text: str, box: str = "AI"):
    # text = text.replace(f"ChatBot:", "").replace("Human:", "")

    if box == "human":
        textbox_human = html.Div(
            html.Div(text, className="message-box"),
            className="message-box-wrapper",
        )

        return html.Div([textbox_human], className="message-wrapper reverse")
    elif box == "AI":
        textbox = html.Div(
            html.Div(text, className="message-box"),
            className="message-box-wrapper",
        )

        return html.Div([textbox], className="message-wrapper ")

    else:
        raise ValueError("Incorrect option for `box`.")
