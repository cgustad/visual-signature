import dash
import dash_bootstrap_components as dbc
from layout.css import SIDEBAR_STYLE
from dash import Input, Output, dcc, html

sidebar = html.Div(
    [
        html.H2("Signatures", className="display-4"),
        html.Hr(),
        html.P("Analysis of Gguf files", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Backends", href="/", active="exact"),
                dbc.NavLink("Text", href="/text", active="exact"),
                dbc.NavLink("Points", href="/models", active="exact"),
                dbc.NavLink("Tests", href="/tests", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)
