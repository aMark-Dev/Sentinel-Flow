# Sentinel Flow

# Sentinel Flow: Previsão de Variação Volumétrica com IA

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.0-blue.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3-orange.svg)

Este repositório contém o código e os dados para o projeto "Sentinel Flow", uma iniciativa de ciência de dados para modelar e prever a variação diária de volume em reservatórios do semiárido brasileiro, utilizando dados públicos de clima e Machine Learning.

---

## Sobre o Projeto

Nascido no Ceará, uma região onde a segurança hídrica é uma questão vital, este projeto surgiu da curiosidade de aplicar a Inteligência Artificial para entender um dos maiores desafios locais: a perda de água por evaporação em nossos reservatórios, conhecidos como "açudes".

O objetivo é construir um modelo de Machine Learning capaz de prever a variação diária de volume (`ΔVolume`) com base em variáveis meteorológicas, servindo como uma ferramenta para estudos de impacto climático e gestão de recursos hídricos.

## Metodologia

O projeto é dividido em duas fases principais:
* **Fase 1 (Protótipo):** Coleta de dados brutos, limpeza, unificação e treinamento de um modelo de base (`RandomForestRegressor`) para validar a viabilidade da abordagem.
* **Fase 2 (Refinamento):** Aplicação de técnicas avançadas de **Engenharia de Features** (Lag Features, Janelas Móveis) e uso de modelos mais potentes (XGBoost) para melhorar a performance e a precisão das previsões.

## Fontes de Dados
* **Dados de Volume dos Reservatórios:** Sistema de Acompanhamento de Reservatórios (SAR) da Agência Nacional de Águas (ANA).
* **Dados Meteorológicos:** Instituto Nacional de Meteorologia (INMET).

## Tecnologias Utilizadas
* **Linguagem:** Python
* **Bibliotecas Principais:**
    * **Pandas:** Para manipulação, limpeza e unificação das séries temporais.
    * **Scikit-learn:** Para treinamento e avaliação dos modelos de Machine Learning.
    * **Matplotlib / Seaborn:** Para visualização e análise de dados.
* **Ferramentas:**
    * **Git & GitHub:** Para controle de versão.
    * **Jupyter Notebook:** Para desenvolvimento e análise exploratória.

## Estrutura do Repositório
* **/ (Raiz):** Contém este README e os notebooks principais.
* **/DF/:** Contém os DataFrames utilizados e salvos durante o projeto, com um `README.md` explicando cada um (Dicionário de Dados).
* **/Fase 1/:** Contém o modelo criado na primeira fase e um `README.md` com a análise detalhada dos resultados e aprendizados.

## Como Executar
1.  Clone este repositório: `git clone https://github.com/seu-usuario/Sentinel-Flow.git`
2.  Crie e ative um ambiente virtual: `python -m venv .venv` e `source .venv/bin/activate` (ou `.\.venv\Scripts\activate` no Windows).
3.  Instale as dependências: `pip install -r requirements.txt` (Crie este arquivo com `pip freeze > requirements.txt`).
4.  Execute os notebooks Jupyter na ordem numérica.

## Autor
* **Marcos Antonio**

---
---

## English Version

# Sentinel Flow: Reservoir Volumetric Change Prediction with AI

This repository contains the code and data for the "Sentinel Flow" project, a data science initiative to model and predict the daily volumetric change in Brazilian semi-arid reservoirs using public weather data and Machine Learning.

## About The Project

Born in Ceará, a Brazilian state where water security is a vital issue, this project stems from the curiosity to apply Artificial Intelligence to understand one of the major local challenges: water loss by evaporation in our reservoirs, known as "açudes".

The goal is to build a Machine Learning model capable of predicting the daily change in volume (`ΔVolume`) based on meteorological variables, serving as a tool for climate impact studies and water resource management.

## Methodology

The project is divided into two main phases:
* **Phase 1 (Prototype):** Raw data collection, cleaning, merging, and training of a baseline model (`RandomForestRegressor`) to validate the approach's feasibility.
* **Phase 2 (Refinement):** Application of advanced **Feature Engineering** techniques (Lag Features, Rolling Windows) and the use of more powerful models (XGBoost) to improve the performance and accuracy of the predictions.

## Data Sources
* **Reservoir Volume Data:** Reservoir Monitoring System (SAR) from the National Water Agency of Brazil (ANA).
* **Meteorological Data:** National Institute of Meteorology of Brazil (INMET).

## Technologies Used
* **Language:** Python
* **Core Libraries:**
    * **Pandas:** For time-series manipulation, cleaning, and merging.
    * **Scikit-learn:** For training and evaluating Machine Learning models.
    * **Matplotlib / Seaborn:** For data visualization and analysis.
* **Tools:**
    * **Git & GitHub:** For version control.
    * **Jupyter Notebook:** For exploratory analysis and iterative development.

## Repository Structure
* **/ (Root):** Contains this README and the main notebooks.
* **/DF/:** Contains the DataFrames used and saved throughout the project, with a `README.md` explaining each one (Data Dictionary).
* **/Fase 1/:** Contains the model created in the first phase and a `README.md` with a detailed analysis of the results and lessons learned.

## How to Run
1.  Clone this repository: `git clone https://github.com/your-username/Sentinel-Flow.git`
2.  Create and activate a virtual environment: `python -m venv .venv` and `source .venv/bin/activate` (or `.\.venv\Scripts\activate` on Windows).
3.  Install dependencies: `pip install -r requirements.txt` (Create this file with `pip freeze > requirements.txt`).
4.  Run the Jupyter notebooks in numerical order.

## Author
* **Marcos Antonio**
