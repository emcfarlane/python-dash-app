from dash import Dash, dcc, html

from . import ids


def render(app: Dash) -> html.Div:
    all_stocks = ["aapl", "amzn", "meta", "goog", "msft"]

    return html.Div(children=[
        html.H6("Stocks"),
        dcc.Dropdown(
            id=ids.DROPDOWN,
            options=[{
                "label": ticker.upper(),
                "value": ticker,
            } for ticker in all_stocks],
            value=all_stocks[0],
            multi=False,
        ),
    ])
