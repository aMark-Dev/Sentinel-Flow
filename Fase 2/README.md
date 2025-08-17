# Análise do Modelo da Fase 2: Engenharia de Features e XGBoost

## Objetivo da Fase 2
Após a análise da Fase 1, que resultou em um R² negativo, a hipótese principal era que o modelo de base carecia de contexto temporal. O objetivo da Fase 2 era, portanto, enriquecer o dataset com "memória" e aplicar um algoritmo mais potente para capturar relações complexas.

As duas estratégias principais foram:
1.  **Engenharia de Features:** Criação de *Lag Features* (variáveis defasadas no tempo) para as principais colunas de clima (temperatura, radiação, etc.) dos 3 dias anteriores.
2.  **Modelo Avançado:** Substituição do `RandomForestRegressor` pelo `XGBoost` (`XGBRegressor`), um algoritmo de Gradient Boosting conhecido por sua alta performance em dados tabulares.

## Processo Técnico e Desafios

### 1. Criação das Lag Features
Utilizando o método `.shift()` do Pandas, foram criadas 15 novas colunas, representando os valores de 5 variáveis climáticas principais para `t-1`, `t-2` e `t-3` dias.

### 2. Tratamento da Variável Alvo
O resultado inicial do XGBoost foi um R² de **-21.5**, ainda pior que o da Fase 1, apesar do MAE continuar baixo. A análise indicou que os valores muito pequenos da variável alvo (`variacao_volume`, ex: -0.02) estavam causando instabilidade numérica no processo de otimização iterativo do XGBoost.

**Solução:** A variável alvo foi escalada por um fator de 1.000.000 para ser representada em metros cúbicos (m³) em vez de hectômetros cúbicos (hm³), tornando os valores mais estáveis para o algoritmo.

### 3. Detecção e Correção de Data Leakage (Vazamento de Dados)
Mesmo com a escala corrigida, um novo treinamento resultou em um R² "perfeito" de **0.99**. A análise de importância das features (`feature_importances_`) revelou a causa: o modelo estava usando a própria variável alvo (que permaneceu acidentalmente no conjunto de features `X`) para fazer a previsão, um caso clássico de *data leakage*.

**Solução:** A definição do conjunto de features `X` foi corrigida para remover explicitamente todas as versões da variável alvo.

## Resultados Finais da Fase 2
Após a correção do *data leakage*, o modelo foi treinado novamente. Os resultados honestos foram:
* **Score R²:** -0.3334
* **Erro Absoluto Médio (MAE):** 15,141 m³ (ou 0.015 hm³)

A análise de importância das features mostrou que o modelo estava focando massivamente na **precipitação** (atual e dos dias anteriores), respondendo por mais de 70% da "atenção" do modelo.

## Principal Insight e Lições Aprendidas

A principal lição desta fase foi profunda: mesmo com features temporais e um modelo potente, o "sinal" sutil da evaporação era completamente ofuscado pelo "ruído" de duas variáveis de grande impacto, mas não medidas: o **consumo de água** (humano/agrícola) e o **aporte dos rios** ao reservatório.

O modelo focava na chuva (o maior sinal de entrada de água), mas não conseguia explicar a variação nos dias sem chuva porque os sinais de saída (consumo) e entrada (rios) eram desconhecidos e dominantes.

O resultado negativo do R² nesta fase não foi um fracasso de modelagem, mas sim a **confirmação científica de que uma abordagem puramente preditiva com os dados públicos disponíveis era inviável.** Este insight foi o catalisador para a mudança estratégica para a Fase 3.

---
---

## English Version

# Phase 2 Model Analysis: Feature Engineering and XGBoost

## Objective of Phase 2
Following the analysis of Phase 1, which resulted in a negative R² score, the main hypothesis was that the baseline model lacked temporal context. The objective of Phase 2 was, therefore, to enrich the dataset with "memory" and apply a more powerful algorithm to capture complex relationships.

The two primary strategies were:
1.  **Feature Engineering:** Creation of *Lag Features* (time-delayed variables) for the main climate columns (temperature, radiation, etc.) from the previous 3 days.
2.  **Advanced Model:** Replacement of the `RandomForestRegressor` with `XGBoost` (`XGBRegressor`), a Gradient Boosting algorithm known for its high performance on tabular data.

## Technical Process and Challenges

### 1. Lag Feature Creation
Using the `.shift()` method in Pandas, 15 new columns were created, representing the values of 5 key climate variables for `t-1`, `t-2`, and `t-3` days.

### 2. Target Variable Treatment
The initial result from XGBoost was an R² score of **-21.5**, even worse than in Phase 1, although the MAE remained low. The analysis indicated that the very small values of the target variable (`variacao_volume`, e.g., -0.02) were causing numerical instability in XGBoost's iterative optimization process.

**Solution:** The target variable was scaled by a factor of 1,000,000 to be represented in cubic meters (m³) instead of cubic hectometers (hm³), making the values more stable for the algorithm.

### 3. Data Leakage Detection and Correction
Even with the corrected scale, a new training run resulted in a "perfect" R² of **0.99**. The feature importance analysis (`feature_importances_`) revealed the cause: the model was using the target variable itself (which had accidentally remained in the feature set `X`) to make its prediction, a classic case of data leakage.

**Solution:** The definition of the feature set `X` was corrected to explicitly remove all versions of the target variable.

## Final Results of Phase 2
After correcting the data leakage, the model was retrained. The honest results were:
* **R² Score:** -0.3334
* **Mean Absolute Error (MAE):** 15,141 m³ (or 0.015 hm³)

The feature importance analysis showed that the model was overwhelmingly focusing on **precipitation** (current and from previous days), accounting for over 70% of the model's "attention".

## Main Insight and Lessons Learned

The main lesson from this phase was profound: even with temporal features and a powerful model, the subtle "signal" of evaporation was completely overshadowed by the "noise" of two high-impact, unmeasured variables: **water consumption** (human/agricultural) and **river inflow** to the reservoir.

The model focused on rainfall (the largest water input signal) but could not explain the variation on days without rain because the output signals (consumption) and other input signals (river inflow) were unknown and dominant.

The negative R² score in this phase was not a modeling failure but rather the **scientific confirmation that a purely predictive approach with the available public data was unfeasible.** This insight was the catalyst for the strategic pivot to Phase 3.