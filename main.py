from dash import Dash, dcc, html
import modules.signup_graphs as sg
import modules.enrolled_graphs as eg

# INTIALIZING SERVER=================== #
app = Dash(__name__)
app.title = 'Introcomp'

text_style = {
    'textAlign': 'center',
    'color': sg.colors['text'],
    'marginBottom': 0
}

spacer_style = {
    'height': '70px',
    'width': '100vw'
}

# CREATING PAGE STRUCTURE============================================================== #
app.layout = html.Div(style={'backgroundColor': sg.colors['background']}, children=[
    html.H1(children='Análise de inscritos no Introcomp 2023', style=text_style),
    html.P(children=f'Total de inscritos: {sg.total_enrollments}', style=text_style),
    html.H2(children='Sabe programar', style=text_style),
    dcc.Graph(id='kpg', figure=sg.knows_programming),
    html.H2(children='Tem computador', style=text_style),
    dcc.Graph(id='hcg', figure=sg.has_computer),
    html.H2(children='Tipo da escola', style=text_style),
    dcc.Graph(id='ctb', figure=sg.schooltype_bar_graph),
    html.Div(style=spacer_style),
    dcc.Graph(id='sgr', figure=sg.school_grade_relation),
    html.Div(style=spacer_style),
    html.H2(children='Cidade / Bairro', style=text_style),
    html.H3(children='Residência', style=text_style),
    dcc.Graph(id='hcp', figure=sg.housecity_pie_graph),
    dcc.Graph(id='hdb', figure=sg.districts_bar_graph),
    html.Div(style=spacer_style),
    html.H3(children='Escola', style=text_style),
    dcc.Graph(id='pbg', figure=sg.schoolcity_pie_graph),
    html.Div(style=spacer_style),
    html.H2(children='Genêro', style=text_style),
    dcc.Graph(id='gpg', figure=sg.gender_proportion),
    dcc.Graph(id='gkp', figure=sg.gender_program),
    html.Div(style=spacer_style),
    html.H2(children='Escolaridade', style=text_style),
    dcc.Graph(id='gg', figure=sg.grade_graph),
    html.Div(style=spacer_style),
    html.H3(children='Sabem programar, por escolaridade', style=text_style),
    dcc.Graph(id='pbg', figure=sg.program_grade_graph),

    html.Div(style=spacer_style),
    html.Div(style=spacer_style),
    html.Div(style=spacer_style),

    html.H1(children='Análise de matriculados no Introcomp 2023', style=text_style),
    html.H2(children='Sabe programar', style=text_style),
    dcc.Graph(id='kpg', figure=eg.knows_programming),
    html.H2(children='Tem computador', style=text_style),
    dcc.Graph(id='hcg', figure=eg.has_computer),
    html.H2(children='Tipo da escola', style=text_style),
    dcc.Graph(id='ctb', figure=eg.schooltype_bar_graph),
    html.Div(style=spacer_style),
    dcc.Graph(id='sgr', figure=eg.school_grade_relation),
    html.Div(style=spacer_style),
    html.H2(children='Cidade / Bairro', style=text_style),
    html.H3(children='Residência', style=text_style),
    dcc.Graph(id='hcp', figure=eg.housecity_pie_graph),
    dcc.Graph(id='hdb', figure=eg.districts_bar_graph),
    html.Div(style=spacer_style),
    html.H3(children='Escola', style=text_style),
    dcc.Graph(id='pbg', figure=eg.schoolcity_pie_graph),
    html.Div(style=spacer_style),
    html.H2(children='Genêro', style=text_style),
    dcc.Graph(id='gpg', figure=eg.gender_proportion),
    dcc.Graph(id='gkp', figure=eg.gender_program),
    html.Div(style=spacer_style),
    html.H2(children='Escolaridade', style=text_style),
    dcc.Graph(id='gg', figure=eg.grade_graph),
    html.Div(style=spacer_style),
    html.H3(children='Sabem programar, por escolaridade', style=text_style),
    dcc.Graph(id='pbg', figure=eg.program_grade_graph),
])

if __name__ == '__main__':
    app.run_server()
