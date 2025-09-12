#importando, exportando e lendo as 5 primeiras linhas
import pandas as pd
medico_df = pd.read_csv('/content/medico_db_atualizado.csv')
medico_df.head()

#lendo a 5 ultimas linhas
medico_df.tail()

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
medico_df.head()

#eliminando duplicatas
medico_df = medico_df.drop_duplicates(subset=['paciente'])
medico_df = medico_df.drop_duplicates(subset=['matricula'])
medico_df.shape

#verificando a eliminação
medico_df.matricula.value_counts()

#resetendo o indice novamente
medico_df = medico_df.reset_index(drop=True)
print(medico_df.shape)
medico_df.tail()

#visualizando a tabela tratada
display(medico_df.head(25))

#botando em csv ja tratado
medico_df.to_csv('medico_db_atualizado.csv', index=False)
medico_csv = pd.read_csv('medico_db_atualizado.csv')
medico_csv.head()

#convertendo para execel para meu professor vizualizar
medico_df.to_excel('medico_db_atualizado.xlsx', index=False)
medico_excel = pd.read_excel('medico_db_atualizado.xlsx')
medico_excel.head()

#eliminando colunas inuteis
medico_df.drop(['idcadmed', 'Idguia', 'nroguia', 'paciente', 'titular',
                'matricula', 'Senha', 'cirurgiao', 'crm_cirurgiao'], axis=1)
