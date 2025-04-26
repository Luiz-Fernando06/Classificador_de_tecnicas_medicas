#importando, exportando e lendo as 5 primeiras linhas e bibliotecas necessarias
import pandas as pd 
from sklearn.preprocessing import LabelEncoder #codificação
from imblearn.over_sampling import SMOTE #biblioteca que gera exemplos sinteticos
medico_df = pd.read_csv('/content/medico_db_atualizado.csv')
medico_df.head(1)

#lendo a 5 ultimas linhas
medico_df.tail(1)

#vendo a quantidade de linhas e colunas
medico_df.shape

#vizualizando as informações e os tipos de dados
medico_df.info()

#verificando quantos valores nulos
medico_df.isnull().sum()

#eliminando valores nulos e vizualizando quantas linhas e colunas sobraram, e se ainda tem valores nulos
medico_df = medico_df.dropna()
print(medico_df.shape)
medico_df.isnull().sum()

#reiniciando os indices das linhas
medico_df = medico_df.reset_index(drop=True)
medico_df.head(1)

#eliminando duplicatas
medico_df = medico_df.drop_duplicates(subset=['paciente'])
medico_df = medico_df.drop_duplicates(subset=['matricula'])
medico_df.shape

#verificando a eliminação
medico_df.matricula.value_counts()

#resetendo o indice novamente
medico_df = medico_df.reset_index(drop=True)
print(medico_df.shape)
medico_df.tail(3)

#visualizando a tabela tratada
display(medico_df.head(3))

#eliminando colunas inuteis
medico_df = medico_df.drop(['idcadmed', 'Idguia', 'nroguia', 'paciente', 'titular',
                'matricula', 'Senha', 'cirurgiao', 'crm_cirurgiao'], axis=1)
medico_df.head(1)

#convertendo para valores numericos as colunas:
#dt_cirurg, data_cadastro, hora_inicio, hora_fim, tipo_cirurgia
medico_df.dt_cirurg = pd.to_datetime(medico_df.dt_cirurg, errors='coerce')
medico_df.data_cadastro = pd.to_datetime(medico_df.data_cadastro, errors='coerce')
medico_df.hora_inicio = pd.to_datetime(medico_df.hora_inicio, errors='coerce')
medico_df.hora_fim = pd.to_datetime(medico_df.hora_fim, errors='coerce')
medico_df.info()

#extraindo informações de dt_cirurg:
# dt_cirurg
medico_df['ano_cirurg'] = medico_df['dt_cirurg'].dt.year
medico_df['mes_cirurg'] = medico_df['dt_cirurg'].dt.month
medico_df['dia_semana_cirurg'] = medico_df['dt_cirurg'].dt.weekday

# data_cadastro
medico_df['ano_cadastro'] = medico_df['data_cadastro'].dt.year
medico_df['mes_cadastro'] = medico_df['data_cadastro'].dt.month
medico_df['dia_semana_cadastro'] = medico_df['data_cadastro'].dt.weekday

# hora_fim e hora_inicio
medico_df['hora_inicio_hora'] = medico_df['hora_inicio'].dt.hour
medico_df['hora_fim_hora'] = medico_df['hora_fim'].dt.hour

# Dropa linhas onde qualquer coluna derivada das datas é nula
medico_df = medico_df.dropna(subset=[
    'ano_cirurg', 'mes_cirurg', 'dia_semana_cirurg',
    'ano_cadastro', 'mes_cadastro', 'dia_semana_cadastro',
    'hora_inicio_hora', 'hora_fim_hora'
])

display(medico_df.head(5))

#dropando as colunas de data antiga
medico_df = medico_df.drop(['dt_cirurg', 'data_cadastro', 'hora_inicio', 'hora_fim'], axis=1)
display(medico_df.head(1))

#verificando se todas as colunas são numericas
display(medico_df.info()) #OBS: So a coluna tipo_cirurgia esta como categorica

#verificando se ta balaanceado ou não
medico_df.tipo_cirurgia.value_counts()

#separando os dados em variaveis de entrada e variaveis alvos para o balanceamento
X = medico_df.drop('tipo_cirurgia', axis=1)
y = medico_df['tipo_cirurgia']

#balanceando os dados
smote = SMOTE(random_state=1) #Gera exemplos sinteticos aleatorios permanentes 
X_balanceamento, y_balanceamento = smote.fit_resample(X, y)

# Verificando o balanceamento
print(y_balanceamento.value_counts())

#numerando a coluna tipo_cirurgia:
enconder = LabelEncoder() #criando um modelo de codificação

#criando nova coluna para codificar e receber os valores de tipo_cirurgia codificados
medico_df['tipo_cirurgia_enconder'] = enconder.fit_transform(medico_df['tipo_cirurgia'])
medico_df.tail(10)

#Dropando a coluna antiga
medico_df = medico_df.drop('tipo_cirurgia', axis=1)
medico_df.head(1)

#balanceado a nova couluna
X = medico_df.drop('tipo_cirurgia_enconder', axis=1)
y = medico_df['tipo_cirurgia_enconder']

smote = SMOTE(random_state=1)  
X_balanceamento, y_balanceamento = smote.fit_resample(X, y)

#verificando o balanceamento
print(y_balanceamento.value_counts()) #ok
