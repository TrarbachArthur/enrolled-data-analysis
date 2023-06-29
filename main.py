from dash import Dash, dcc, html
import modules.graphs as gp

# INTIALIZING SERVER=================== #
app = Dash(__name__)
app.title = 'Introcomp'

text_style = {
    'textAlign': 'center',
    'color': gp.colors['text'],
    'marginBottom': 0
}

# CREATING PAGE STRUCTURE============================================================== #
app.layout = html.Div(style={'backgroundColor': gp.colors['background']}, children=[
    html.H1(children='Análise de inscritos no Introcomp 2023', style=text_style),
    html.H2(children='Escolaridade', style=text_style),
    dcc.Graph(id='gg', figure=gp.grade_graph),
    html.H3(children='Sabem programar, por escolaridade', style=text_style),
    dcc.Graph(id='pbg', figure=gp.program_grade_graph)
    html.H2(children='Genêro', style=text_style),
    dcc.Graph(id='gg', figure=gp.grade_graph)
])

if __name__ == '__main__':
    app.run_server()
