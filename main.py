from dash import Dash, html
from flask import Flask
from os import environ
from src.components.layout import create_layout

app = Flask(__name__)
dash_app = Dash(__name__, server=app, url_base_pathname="/dash/")
dash_app.title = "Dash App"
dash_app.layout = create_layout(dash_app)


@app.route('/health')
def health():
    return 'OK'


@app.route("/")
def index():
    return dash_app.index()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(environ.get("PORT", 8080)))
