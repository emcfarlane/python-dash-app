from dash import Dash, html

from . import chart, dropdown


def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    dropdown.render(app),
                ],
            ),
            chart.render(app),
        ],
    )
