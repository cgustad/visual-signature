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
        content,
    ]
)

# Update content based on sidebar selection
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.P("Oh cool, this is backends page")
    elif pathname == "/text":
        return html.P("Oh cool, this is a text page")
    elif pathname == "/points":
        return html.P("Oh cool, this is a point page")
    elif pathname == "/tests":
        return html.P("Oh cool, this is test page!")
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )



# Run the app
if __name__ == '__main__':
    app.run(debug=True)
