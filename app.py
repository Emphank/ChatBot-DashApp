import dash_bootstrap_components as dbc
from dash import Dash
import openai
import os

APP_TITLE = "Chatbot App"

app = Dash(
    __name__,
    title=APP_TITLE,
    update_title="Loading...",
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.FLATLY],
)

openai.api_key = os.getenv("OPENAI_API_KEY")

print(openai.api_key)
