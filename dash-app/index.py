import dash
from dash.dependencies import Input, Output
import dash_design_kit as ddk
import dash_core_components as dcc
import dash_html_components as html
import dash_table

import sys
import os
import utils as utils

from app import app
import pages
server = app.server


# to view standalone Dash app locally, set utils.py/HOST_APP_PATHNAME = '/'
# or use env variable IGNORE_HOST_APP_PATHNAME = 'true'
if 'IGNORE_HOST_APP_PATHNAME' in os.environ and os.environ['IGNORE_HOST_APP_PATHNAME'].upper() == 'TRUE':
    strip_relative_path = app.strip_relative_path
    get_relative_path = app.get_relative_path
else:
    strip_relative_path = utils.strip_host_relative_path
    get_relative_path = utils.get_host_relative_path


app.layout = ddk.App([
    ddk.Header([
        ddk.Logo(src=utils.embedded_asset_url('logo.png')),
        ddk.Title('Analytics'),
        ddk.Menu([
            dcc.Link(
                href=get_relative_path('/'),
                children='Home'
            ),
            dcc.Link(
                href=get_relative_path('/historical-view'),
                children='Historical View'
            ),
            dcc.Link(
                href=get_relative_path('/predicted-view'),
                children='Predicted View'
            ),
        ])
    ]),

    dcc.Location(id='url'),
    html.Div(id='content')
])


@app.callback(Output('content', 'children'), [Input('url', 'pathname')])
def display_content(pathname):
    page_name = strip_relative_path(pathname)
    if not page_name:  # None or ''
        return pages.home.layout
    elif page_name == 'historical-view':
        return pages.historical_view.layout
    elif page_name == 'predicted-view':
        return pages.predicted_view.layout


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=True, dev_tools_hot_reload=True)
