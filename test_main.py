# 1. imports of your dash app
import dash
from dash import html

from main import dash_app


# 2. give each testcase a test case ID, and pass the fixture
# dash_duo as a function argument
def test_001_child_with_0(dash_duo):
    app = dash.Dash(__name__)
    app.layout = html.Div(id="nully-wrapper", children=0)

    # start the app
    dash_duo.start_server(dash_app)

    # Wait for the core app components to be loaded in the browser
    dash_duo.wait_for_element("#dropdown", timeout=4)
    dash_duo.wait_for_element("#chart", timeout=4)

    # Assert that there are no errors in the browser console
    assert dash_duo.get_logs() == [], "browser console should contain no error"

    # Take a snapshot for visual diffing, stored in /tmp/dash_artifacts
    dash_duo.take_snapshot("test_001_child_with_0-layout")
