from dash import Dash, dcc, html
import modules.graphs as gp

# INTIALIZING SERVER=================== #
app = Dash(__name__)
app.title = 'Introcomp'

text_style = {
    'textAlign': 'center',
    'color': gp.colors['text']
}

# CREATING PAGE STRUCTURE============================================================== #
app.layout = html.Div(style={'backgroundColor': gp.colors['background']}, children=[
    
])

if __name__ == '__main__':
    app.run_server()
