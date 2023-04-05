from dash import Dash, dcc, html, Input, Output
from functools import lru_cache
import plotly.graph_objects as go
import requests
import json
import time

from . import ids


@lru_cache()
def load_stock_data(stock, interval='1d', range='1mo', ttl_hash=None):
    """
    queries yahoo finance api to receive stock information
    
    parameters: 
        stock - short-handle identifier of the company
        interval - time interval between each data point
        range - time range of the data
    
    returns a list of comma seperated value lines
    """
    del ttl_hash

    with requests.session():
        url = 'https://query1.finance.yahoo.com/v8/finance/chart/' \
              '{stock}?interval={interval}&range={range}' \
              .format(stock=stock, interval=interval, range=range)

        raw = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        json_data = json.loads(raw.text)
        return json_data


def get_ttl_hash(seconds=3600):
    """Return the same value within `seconds` time period"""
    return round(time.time() / seconds)


def render(app: Dash) -> html.Div:

    @app.callback(
        Output(ids.CHART, "children"),
        [
            Input(ids.DROPDOWN, "value"),
        ],
    )
    def update_chart(stock: str) -> html.Div:
        if not stock:
            return html.Div('No stock selected', id=ids.CHART)

        data = load_stock_data(stock, ttl_hash=get_ttl_hash())
        stock_data = data['chart']['result'][0]

        fig = go.Figure(
            go.Candlestick(
                x=stock_data['timestamp'],
                open=stock_data['indicators']['quote'][0]['open'],
                high=stock_data['indicators']['quote'][0]['high'],
                low=stock_data['indicators']['quote'][0]['low'],
                close=stock_data['indicators']['quote'][0]['close'],
            ))

        return html.Div(dcc.Graph(figure=fig), id=ids.CHART)

    return html.Div(id=ids.CHART)
