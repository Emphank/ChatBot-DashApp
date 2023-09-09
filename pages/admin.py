from dash import html, dcc
from dash.dependencies import Input, Output, State
from app import app

import dash_bootstrap_components as dbc
import json


def admin():
    return html.Div(
        [
            html.Div(
                [
                    html.Div(
                        "Context Configuration",
                        style={
                            "font": "25px Poppins Bold",
                            "fontWeight": "bold",
                            "padding": "0 0 26px",
                        },
                    ),
                    dcc.Textarea(
                        id="context",
                        placeholder="Enter the context",
                        style={
                            "width": "100%",
                            "height": "120px",
                            "border-radius": "20px",
                            "outline": "none",
                            "padding": "10px",
                            "border": "solid 3px #98d4f3",
                            "margin-bottom": "30px",
                            "resize": "none",
                            "overflow": "auto",
                        },
                    ),
                    dcc.Input(
                        id="password",
                        type="password",
                        placeholder="Enter the password",
                        style={
                            "font-size": "15px",
                            "color": "#555",
                            "width": "100%",
                            "height": "45px",
                            "padding": "0 5px",
                            "outline": "none",
                            "border": "none",
                            "line-height": "1.2",
                            "touch-action": "manipulation",
                            "border-bottom": "2px solid",
                            "margin-bottom": "30px",
                        },
                    ),
                    html.Button(
                        "Save",
                        id="save-button",
                        style={
                            "font-family": "Poppins-Medium",
                            "font-size": "15px",
                            "color": "#fff",
                            "line-height": 1.2,
                            "text-transform": "uppercase",
                            "display": "flex",
                            "justify-content": "center",
                            "align-items": "center",
                            "padding": "0 20px",
                            "width": "100%",
                            "height": "50px",
                            "border": "none",
                            "outline": "none",
                            "background": "-webkit-linear-gradient(right,#21d4fd,#b721ff,#21d4fd,#b721ff)",
                            "z-index": 1,
                            "border-radius": "25px",
                        },
                    ),
                ],
                style={
                    "height": "auto",
                    "width": "390px",
                    "padding": "77px 55px 33px",
                    "display": "flex",
                    "flex-direction": "column",
                    "justify-content": "center",
                    "gap": "20px",
                    "align-items": "center",
                    "border-radius": "10px",
                    "background": "#fff",
                },
            ),
            html.Div(id="output-div", style={"marginTop": "20px"}),
        ],
        style={
            "height": "100vh",
            "display": "flex",
            "justify-content": "center",
            "align-items": "center",
            "background": "#f2f2f2",
        },
    )


@app.callback(
    Output("output-div", "children"),
    Output("save-button", "n_clicks"),
    Input("save-button", "n_clicks"),
    State("context", "value"),
    State("password", "value"),
)
def handle_button_click(n_clicks, context, entered_password):
    correct_password = "password"
    if n_clicks:
        if entered_password == correct_password:
            context_data = {"context": context}

            with open("./context.json", "w") as file:
                json.dump(context_data, file, indent=4)

            return dcc.Location(pathname="/chatbot", id="navigate"), None
        else:
            alert = (
                dbc.Alert(
                    "Incorrect password. Please try again.",
                    color="danger",
                    dismissable=True,
                ),
            )

            return alert, None

    return None, None
