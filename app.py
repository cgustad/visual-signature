from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from layout.sidebar import sidebar
from layout.css import CONTENT_STYLE


# Initialize the app
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP],suppress_callback_exceptions=True)

# Define content
content = html.Div(id="page-content", style=CONTENT_STYLE)
# Set layout
app.layout = html.Div(
    [
        dcc.Location(id="url"),
        sidebar,
        html.H1("HELLO WORKLD!")
    ]
)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
