import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from plotly.subplots import make_subplots

# ----- Registrations ----- #

all_signup = pd.read_csv("./data/Inscricoes2023.csv")
all_signup['name'] = all_signup['name'].str.lower()
enrolled = pd.read_csv("./data/Matriculados2023-simplified.csv")
enrolled['name'] = enrolled['name'].str.lower()
enrolled['marker'] = 1

#print(enrolled)

joined = pd.merge(all_signup, enrolled, on=['name'], how='left')

#print(joined)

df = joined[((pd.notnull(joined['marker'])))]

#print(df['genero'])

for name in enrolled['name']:
    achou = 0
    for name2 in joined['name']:
        if name == name2:
            achou = 1
            break

    if (not achou):
        print(name)

# -------- General info -------- #

total_enrollments = df.shape[0]

# -------- School type -------- #

tipoEscola = df["tipo escola"].value_counts()
grade_school = df[df['escolaridade'].str.contains('2006') == False]
escolaridade_school = grade_school['escolaridade'].value_counts()

grade_school['escola tipo'] = grade_school['tipo escola']
scolarity_by_schooltype = grade_school.pivot_table(values='escola tipo', index=['tipo escola', 'escolaridade'], aggfunc='count').reset_index()
scolarity_by_schooltype = scolarity_by_schooltype.reindex(index=scolarity_by_schooltype.index[::-1])

# -------- City / District --------#

contagem_cidade_moram = df['cidade'].value_counts().reset_index()
contagem_cidade_moram.columns = ['Cidades', 'Quantidade']
contagem_cidade_escola = df['cidade escola'].value_counts().reset_index()
contagem_cidade_escola.columns = ['Cidades Escola', 'Quantidade']
contagem = df['bairro'].value_counts().head(20).reset_index() # contagem dos 15 bairros mais frequentes
contagem.columns = ['Bairro', 'Frequência']

# filtrar df para apenas os bairros mais frequentes
bairros_frequentes = df[df['bairro'].isin(contagem)]

# -------- Grade -------- #

grade = df[df['escolaridade'].str.contains('2006') == False]
escolaridade = grade['escolaridade'].value_counts()

grade['programar'] = grade['sabe programar']
program_by_grade = grade.pivot_table(values='programar', index=['sabe programar', 'escolaridade'], aggfunc='count').reset_index()

# -------- Gender -------- #

subs_data = df.drop(["data da inscrição", "edição", "turno", "nascimento", "bairro", "cidade", "email", "escola", "cidade escola", "tipo escola"], axis='columns')
subs_data.set_index("name", inplace = True)
df_Teste = subs_data.iloc[:,4]
a = pd.DataFrame(subs_data.iloc[:,0])
gender_data = a.join(df_Teste)

qtd_meninas=0
qtd_meninos=0
meninas_sabem=0
meninos_sabem=0
for i in range (36):
    if(df_Teste.iloc[i]=="female"):
        qtd_meninas=qtd_meninas+1
        if(gender_data.iloc[i, 0]==True):
            meninas_sabem=meninas_sabem+1
    else :
        qtd_meninos=qtd_meninos+1
        if(gender_data.iloc[i, 0]==True):
            meninos_sabem=meninos_sabem+1

# -------- Graphs -------- #

### SCHOOL TYPE ###

schooltype_bar_graph = px.bar(tipoEscola, y='count', x=['Estadual', 'Federal', 'Municipal'])
schooltype_bar_graph.update_layout(yaxis_title='Quantidade de Inscritos', xaxis_title='')

school_grade_relation = px.bar(scolarity_by_schooltype, x='escolaridade', y='escola tipo', color='tipo escola')
school_grade_relation.update_layout(yaxis_title='Tipo da escola', xaxis_title='')
school_grade_relation.update_xaxes(autorange='reversed')

### CITY ###

housecity_pie_graph = px.pie(contagem_cidade_moram, values = 'Quantidade', names = 'Cidades')
schoolcity_pie_graph = px.pie(contagem_cidade_escola, values = 'Quantidade', names = 'Cidades Escola')
districts_bar_graph = px.bar(contagem, x='Bairro', y='Frequência')

### GRADE ###

grade_graph = px.pie(escolaridade, values='count', names=escolaridade.index)
grade_graph.update_traces(textinfo='percent+value')

program_grade_graph = px.histogram(program_by_grade, x='escolaridade', y='programar', color='sabe programar', color_discrete_sequence=['red', 'green'])
program_grade_graph.update_layout(yaxis_title='Sabe programar', xaxis_title='')

### GENDER ###

nomes = ['MENINAS', 'MENINOS'] 
data = [qtd_meninas, qtd_meninos] 
gender_proportion = px.pie(data, values=data, names = nomes, color_discrete_sequence=["blue", "red"])
gender_proportion.update_traces(textinfo='percent+value')

nomes = ['SABEM PROGRAMAR', 'NÃO SABEM'] 
data = [meninas_sabem, qtd_meninas-meninas_sabem] 
female_program = go.Pie(values=data, labels = nomes, title = "MENINAS", textinfo = 'percent+value', marker_colors=["#eba834", "#f7e754"])
#, color_discrete_sequence=["#eba834", "#f7e754"]

nomes = ['SABEM PROGRAMAR', 'NÃO SABEM'] 
data = [meninos_sabem, qtd_meninos-meninos_sabem] 
male_program = go.Pie(values=data, labels = nomes, title = "MENINOS", textinfo = 'percent+value', marker_colors=["#405394", "#60a1eb"])
#, color_discrete_sequence=["#405394", "#60a1eb"]

gender_program = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "pie"}]])
gender_program.add_trace(female_program, row = 1, col = 1)
gender_program.add_trace(male_program, row = 1, col = 2)

### KNOWS PROGRAMMING ###

total_programming = df['sabe programar'].value_counts()
knows_programming = px.pie(total_programming, values='count', names=total_programming.index, color_discrete_sequence=["blue", "red"])
knows_programming.update_traces(textinfo = 'percent+value')

### HAS COMPUTER ###

total_has_pc = df['tem computador'].value_counts()
has_computer = px.pie(total_has_pc, values='count', names=total_has_pc.index, color_discrete_sequence=["blue", "red"])
has_computer.update_traces(textinfo = 'percent+value')

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

gender_proportion.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

gender_program.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

housecity_pie_graph.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

schoolcity_pie_graph.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

districts_bar_graph.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

schooltype_bar_graph.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

school_grade_relation.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

knows_programming.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

has_computer.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)