import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from modules.df_manage import extract_data_and_amount, filter_dataframe

# ----- Registrations ----- #
df = pd.read_csv("./data/Inscricoes2023.csv");

# -------- Grade -------- #

grade = df[df['escolaridade'].str.contains('2006') == False]
escolaridade = grade['escolaridade'].value_counts()

grade['programar'] = grade['sabe programar']
program_by_grade = grade.pivot_table(values='programar', index=['sabe programar', 'escolaridade'], aggfunc='count').reset_index()

# ----- Graphs ----- #
grade_graph = px.pie(escolaridade, values='count', names=escolaridade.index)
grade_graph.update_traces(textinfo='percent+value')

program_grade_graph = px.histogram(program_by_grade, x='escolaridade', y='programar', color='sabe programar', color_discrete_sequence=['red', 'green'])
program_grade_graph.update_layout(yaxis_title='Sabe programar', xaxis_title='')

# ----- Editing graphs layouts ----- #
colors = {
    'background': '#020220',
    'text': '#FFFFFF'
}

grade_graph.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

program_grade_graph.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)