# 🏥 Classificador de Técnicas Cirúrgicas


Este projeto é um classificador de técnicas cirúrgicas que utiliza aprendizado de máquina para prever a técnica usada em cirurgias com base em dados do médico, urgência, tipo de acomodação e tipo de cirurgia.

O programa oferece dois modelos de classificação:

Árvore de Decisão (Decision Tree)

Máquina de Vetores de Suporte (SVM)

Ele permite ao usuário:

Avaliar o desempenho dos modelos com base em dados de teste.

Visualizar a árvore de decisão.

Fazer novas classificações inserindo os dados manualmente.

⚙️ Tecnologias utilizadas

Python 3 – Linguagem principal do projeto.

Pandas – Manipulação e organização dos dados.

Scikit-learn – Modelos de aprendizado de máquina (Decision Tree e SVM).

Matplotlib – Visualização da árvore de decisão.

📝 Como funciona

O script carrega um dataset tratado (medico_db_TotalemnteTratado.csv) contendo informações sobre médicos, tipos de cirurgia, urgência e acomodação.

Divide os dados em treino e teste usando train_test_split.

Treina dois modelos de classificação:

DecisionTreeClassifier

SVC (Support Vector Machine)

Exibe um menu interativo para o usuário escolher o modelo e realizar ações como:

Avaliar desempenho (accuracy_score).

Visualizar o desenho da árvore (para Decision Tree).

Fazer novas classificações inserindo dados manualmente.

🖥️ Como usar
1. Instalar dependências
pip install pandas scikit-learn matplotlib

2. Executar o script
python classificador_tecnicas.py

3. Importar o arquivo
medico_dbTotalmentetratado.csv

4. Menu interativo

Escolha o modelo desejado (Árvore de Decisão ou SVM).

Siga as instruções para visualizar desempenho, gerar novas classificações ou desenhar a árvore.

Digite 3 no menu principal para sair.

📊 Exemplo de uso

Ao selecionar Árvore de Decisão e mostrar desempenho, o programa exibirá a acurácia do modelo.

Ao selecionar fazer nova classificação, o usuário insere dados como:

Id do médico

Tipo de urgência (0: não urgente, 1: urgente)

Tipo de cirurgia (0–5)

Tipo de acomodação (1 ou 2)

O classificador então retorna a técnica mais provável: PADRÃO (cirurgia aberta) ou VIDEOLAPAROSCOPIA.

🎯 Objetivo

O projeto foi desenvolvido para:

Automatizar a previsão de técnicas cirúrgicas com base em dados históricos.

Permitir simulações interativas para novos casos médicos.

Demonstrar o uso prático de Decision Tree e SVM em classificação supervisionada.
