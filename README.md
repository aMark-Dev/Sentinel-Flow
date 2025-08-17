# Sentinel Flow: Modelo Analítico da Evaporação em Reservatórios do Semiárido

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.x-blue.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.x-orange.svg)
![XGBoost](https://img.shields.io/badge/XGBoost-3.x-green.svg)

Este repositório documenta a jornada de pesquisa e desenvolvimento do projeto "Sentinel Flow", uma investigação em ciência de dados sobre a modelagem da perda de água em reservatórios no semiárido brasileiro, utilizando dados públicos e aplicando tanto técnicas de Machine Learning quanto modelos analíticos baseados em física.

---

## Sobre o Projeto

Nascido no Ceará, Brasil, uma região onde a segurança hídrica é uma questão de importância crítica, este projeto começou com uma pergunta aparentemente simples: "É possível usar dados de clima para prever a variação diária de volume de um reservatório (açude) com Inteligência Artificial?".

A investigação evoluiu de um modelo preditivo para um **modelo analítico**, após a constatação de que variáveis não-medidas (como consumo de água e aporte de rios) introduziam um ruído significativo que limitava a performance dos algoritmos de Machine Learning.

O objetivo final do projeto tornou-se, então, mais focado e cientificamente robusto: **calcular a taxa de evapotranspiração diária (ETo)** a partir de dados meteorológicos e analisar seus padrões sazonais, servindo como uma ferramenta valiosa para a compreensão do balanço hídrico da região.

## Metodologia: Uma Jornada em Três Fases

A metodologia deste projeto reflete um ciclo de pesquisa iterativo, progredindo em complexidade e adaptando a estratégia com base nas evidências.

### Fase 1: Modelo Preditivo de Base (Baseline)
* **Objetivo:** Testar a hipótese inicial de que dados climáticos de um dia (`t`) poderiam prever a variação de volume (`ΔV`) nesse mesmo dia.
* **Técnica:** Foi treinado um modelo `RandomForestRegressor`.
* **Resultado:** O modelo resultou em um **R² negativo (-0.36)**, provando que a relação direta era inviável e que o modelo performava pior do que uma simples média. A análise completa está no diretório `/Fase 1`.

### Fase 2: Modelo Preditivo Avançado
* **Objetivo:** Aprimorar o modelo base, fornecendo-lhe "memória" através de Engenharia de Features e utilizando um algoritmo mais potente.
* **Técnica:** Foram criadas **Lag Features** (dados climáticos de `t-1`, `t-2`, `t-3` dias) e o modelo foi substituído por um `XGBoost`.
* **Resultado:** Apesar dos ajustes, o R² continuou negativo, e a análise de importância das features revelou que o "sinal" da evaporação era completamente ofuscado pelo "ruído" de variáveis não-medidas (consumo e aporte). A análise completa está no diretório `/Fase 2`.

### Fase 3: Pivô para Modelo Analítico (Resultado Final)
* **Objetivo:** Mudar a pergunta. Em vez de prever a ruidosa `ΔV`, o foco tornou-se **calcular** a evaporação, uma de suas componentes mais importantes.
* **Técnica:** Implementação em Python de um modelo físico-matemático que utiliza a **radiação solar medida** para estimar a evapotranspiração diária, baseado em fatores de conversão da FAO (Organização das Nações Unidas para a Alimentação e a Agricultura).
* **Resultado:** Geração de uma série temporal de evaporação diária (`mm/dia`) com valores fisicamente realistas e um padrão sazonal claro e consistente. A análise está no diretório `/Fase 3`.

## Principais Insights e Conclusões
O resultado final do modelo analítico permitiu as seguintes conclusões:
* A taxa de evaporação na região do Açude Carnaubal exibe uma forte **sazonalidade**, com picos consistentes de até **12 mm/dia** durante a estação seca (segundo semestre do ano).
* A abordagem de Machine Learning preditivo foi ineficaz não por uma falha no algoritmo, mas pela **ausência de variáveis críticas** nos dados públicos, uma lição fundamental em modelagem de sistemas complexos.
* O projeto final entrega uma ferramenta analítica capaz de gerar uma estimativa robusta de evaporação, com potencial de uso em estudos de balanço hídrico.

## Tecnologias e Conceitos
* **Linguagem:** Python
* **Bibliotecas:** Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Seaborn
* **Conceitos:** Análise de Séries Temporais, Engenharia de Features (Lag Features), Modelagem Preditiva (Random Forest, XGBoost), Validação de Modelos (R², MAE), Análise de Importância de Features, Depuração de Modelos (Data Leakage), Modelagem Analítica.
* **Ferramentas:** Git/GitHub, Jupyter Notebook, Ambientes Virtuais (`.venv`)

## Estrutura do Repositório
* **/DF/:** Contém os DataFrames brutos e processados, com seu respectivo Dicionário de Dados.
* **/Fase 1/, /Fase 2/, /Fase 3/:** Contém os notebooks e `READMEs` analíticos para cada fase da investigação.

## Como Executar
1.  Clone este repositório.
2.  Crie e ative um ambiente virtual.
3.  Instale as dependências com `pip install -r requirements.txt`.
4.  Execute os notebooks Jupyter na ordem numérica para reproduzir a análise.

## Autor
* **Marcos Antonio**

---
---

## English Version

# Sentinel Flow: An Analytical Model of Evaporation in Semi-Arid Reservoirs

This repository documents the research and development journey of the "Sentinel Flow" project, a data science investigation into modeling water loss in reservoirs of the Brazilian semi-arid region, applying both Machine Learning techniques and physics-based analytical models.

## About The Project

Originating in Ceará, Brazil, a region where water security is a critically important issue, this project began with a seemingly simple question: "Is it possible to use climate data to predict the daily volume change of a reservoir (known as an 'açude') with Artificial Intelligence?"

The investigation evolved from a predictive model to an **analytical model**, following the discovery that unmeasured variables (such as water consumption and river inflow) introduced significant noise that limited the performance of Machine Learning algorithms.

The project's final objective, therefore, became more focused and scientifically robust: **to calculate the daily reference evapotranspiration (ETo)** from meteorological data and analyze its seasonal patterns, serving as a valuable tool for understanding the region's water balance.

## Methodology: A Three-Phase Journey

The project's methodology reflects an iterative research cycle, progressing in complexity and adapting the strategy based on evidence.

### Phase 1: Baseline Predictive Model
* **Objective:** To test the initial hypothesis that climate data from a given day (`t`) could predict the volume change (`ΔV`) on that same day.
* **Technique:** A `RandomForestRegressor` model was trained.
* **Result:** The model yielded a **negative R² score (-0.36)**, proving the direct relationship was unfeasible and that the model performed worse than a simple average. The full analysis is in the `/Phase 1` directory.

### Phase 2: Advanced Predictive Model
* **Objective:** To improve the baseline model by providing it with "memory" through Feature Engineering and using a more powerful algorithm.
* **Technique:** **Lag Features** (climate data from `t-1`, `t-2`, `t-3` days) were created, and the model was replaced with `XGBoost`.
* **Result:** Despite the adjustments, the R² remained negative. The feature importance analysis revealed that the "signal" of evaporation was completely overshadowed by the "noise" of unmeasured variables (consumption and inflow). The full analysis is in the `/Phase 2` directory.

### Phase 3: Pivot to an Analytical Model (Final Result)
* **Objective:** To change the question. Instead of predicting the noisy `ΔV`, the focus shifted to **calculating** evaporation, one of its most significant components.
* **Technique:** Implementation in Python of a physics-based mathematical model that uses **measured solar radiation** to estimate daily evapotranspiration, based on conversion factors from the FAO (Food and Agriculture Organization of the UN).
* **Result:** Generation of a daily evaporation time series (`mm/day`) with physically realistic values and a clear, consistent seasonal pattern. The analysis is in the `/Phase 3` directory.

## Key Findings and Insights
The final analytical model led to the following conclusions:
* The evaporation rate in the Carnaubal Reservoir region exhibits strong **seasonality**, with consistent peaks of up to **12 mm/day** during the dry season (second half of the year).
* The predictive Machine Learning approach was ineffective not due to an algorithmic failure, but due to the **absence of critical variables** in the public data, a fundamental lesson in modeling complex systems.
* The final project delivers an analytical tool capable of generating a robust estimate of evaporation, with potential use in water balance studies.

## Technologies and Concepts
* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Seaborn
* **Concepts:** Time-Series Analysis, Feature Engineering (Lag Features), Predictive Modeling (Random Forest, XGBoost), Model Validation (R², MAE), Feature Importance Analysis, Model Debugging (Data Leakage), Analytical Modeling.
* **Tools:** Git/GitHub, Jupyter Notebook, Virtual Environments (`.venv`)

## Repository Structure
* **/DF/:** Contains the raw and processed DataFrames, with their respective Data Dictionary.
* **/Fase 1/, /Fase 2/, /Fase 3/:** Contain the notebooks and analytical `READMEs` for each phase of the investigation.

## How to Run
1.  Clone this repository.
2.  Create and activate a virtual environment.
3.  Install dependencies with `pip install -r requirements.txt`.
4.  Run the Jupyter notebooks in numerical order to reproduce the analysis.

## Author
* **Marcos Antonio**
