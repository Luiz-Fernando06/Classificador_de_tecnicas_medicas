# Classificador de Técnicas Médicas — Árvore de Decisão & SVM

## Objetivo:
Desenvolver um sistema interativo para prever a técnica cirúrgica utilizada (Padrão ou Videolaparoscopia) com base em informações clínicas e operacionais, utilizando algoritmos de aprendizado de máquina supervisionado.

## Principais etapas realizadas:

- Pré-processamento de dados: Importação e divisão do dataset em variáveis preditoras (IdMedico, tip_urgencia, tip_acomod, tipo_cirurgia) e variável alvo (tecnica).

- Modelagem:

   - Árvore de Decisão: para visualização interpretável da lógica de classificação.

   - SVM (Support Vector Machine): para comparação de desempenho e robustez preditiva.

   - Avaliação: Medição da acurácia de cada modelo com dados de teste.

   - Interface interativa (CLI): Menus organizados que permitem:

       - Ver desempenho dos modelos.

       - Exibir a árvore de decisão graficamente.

       - Realizar novas previsões informando os dados do paciente.

- Classificação em tempo real: O sistema retorna se a técnica cirúrgica recomendada é “Padrão (Cirurgia Aberta)” ou “Videolaparoscopia”, com base no aprendizado do modelo.

## Resumo:
Projeto de machine learning aplicado à área médica, combinando Decision Tree e SVM em uma interface de console funcional. Ideal para estudos sobre predição de técnicas cirúrgicas e comparação de algoritmos de classificação.
