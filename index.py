from dash.dependencies import Input, Output
from dash import dcc, html, dash

# import pages
from pages.chatbot.chatbot_view import render_chatbot
from pages.chatbot.chatbot_controller import *
from pages.page_not_found import page_not_found
from pages.admin import admin

from app import app


def serve_content():
    """
    :return: html div component
    """
    return html.Div(
        [
            dcc.Location(id="url", refresh=True),
            html.Div(id="page-content"),
        ]
    )


app.layout = serve_content()


@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
    prevent_initial_call=True,
)
def display_page(pathname):
    """
    :param pathname: path of the actual page
    :return: page
    """
    if pathname is None or pathname == "":
        return dash.no_update
    else:
        if pathname in "/" or pathname in "/chatbot":
            return render_chatbot()
        elif pathname in "/admin":
            return admin()
        return page_not_found()


if __name__ == "__main__":
    app.run_server(debug=True)
