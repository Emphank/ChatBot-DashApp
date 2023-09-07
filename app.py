import dash_bootstrap_components as dbc
from dash import Dash
import openai
import os
from dotenv import load_dotenv

load_dotenv()

APP_TITLE = "Chatbot App"

app = Dash(
    __name__,
    title=APP_TITLE,
    update_title="Loading...",
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.FLATLY],
)

openai.api_key = os.getenv("OPENAI_API_KEY")
