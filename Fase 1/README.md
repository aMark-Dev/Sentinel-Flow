# Sentinel Flow

# Análise do Modelo da Fase 1

## Objetivo da Fase 1
O objetivo desta fase era construir um modelo de base (*baseline*) para testar a viabilidade do projeto. A hipótese era que as variáveis meteorológicas de um determinado dia (`t`) poderiam prever a variação de volume do reservatório nesse mesmo dia (`t`).

## Modelo Utilizado
* **Algoritmo:** `RandomForestRegressor` da biblioteca Scikit-learn.
* **Features (Entradas):** Dados diários brutos de precipitação, radiação global, temperatura, umidade e vento.
* **Alvo (Saída):** `variacao_volume`, calculada como `volume_hoje - volume_ontem`.

## Resultados Obtidos
Após o treinamento e a avaliação com dados de teste, os resultados foram:
* **Score R²:** -0.3615
* **Erro Absoluto Médio (MAE):** 0.013 hm³

## Análise dos Resultados: Por que o R² foi Negativo?

Um R² negativo indica que o modelo performou pior do que um modelo simples que apenas previsse a média da variação de volume para todos os dias. O baixo MAE, por outro lado, mostra que o erro médio em termos absolutos era pequeno.

Essa aparente contradição é explicada pela natureza da nossa variável alvo (`variacao_volume`):
1.  **Baixa Variância:** A variação diária de volume de um reservatório massivo é um número muito pequeno, quase sempre próximo de zero.
2.  **Sensibilidade do R²:** A métrica R² penaliza severamente os erros ao quadrado. Em um cenário de baixa variância, mesmo os pequenos erros do modelo (refletidos no baixo MAE) tornam-se proporcionalmente grandes quando elevados ao quadrado, fazendo com que o desempenho do modelo seja pior do que simplesmente usar a média como previsão.

## Principal Insight e Lições Aprendidas

A principal lição desta fase foi que **os dados meteorológicos de um único dia (`t`) não possuem informação suficiente para prever a variação de volume nesse mesmo dia.** Fenômenos como a evaporação têm inércia; a energia absorvida pela água em um dia quente (`t-1`) influencia a evaporação no dia seguinte (`t`), mesmo que este esteja nublado.

O resultado negativo do R² não foi um fracasso, mas sim uma **validação da necessidade da Fase 2**. O modelo de base nos provou que, para capturar a complexidade do problema, é essencial fornecer ao modelo um **contexto temporal**.

Isso direciona o projeto para a **Engenharia de Features**, criando variáveis com "memória" (como *Lag Features* e *Janelas Móveis*) para os próximos modelos.
