# Sentinel Flow

# Dicionário de Dados (Data Dictionary)

Este documento descreve os DataFrames criados e utilizados no projeto "Sentinel Flow".

---

## 1. Dados Brutos

* **`dados_tratados_ana_carnaubal.csv`**
    * **Descrição:** Série histórica do volume diário do Açude Carnaubal, extraída do portal SAR/ANA e processada a partir do arquivo JSON original.
    * **Colunas:**
        * `data` (datetime): Data da medição no formato AAAA-MM-DD.
        * `volume` (float): Volume do reservatório em hectômetros cúbicos (hm³).

* **`clima.csv`**
    * **Descrição:** Série histórica de dados meteorológicos da estação do INMET mais próxima do Açude Carnaubal (Crateús).
    * **Colunas:** Contém diversas variáveis climáticas, como `PRECIPITACAO`, `RADIACAO GLOBAL`, `TEMPERATURA`, etc.

---

## 2. Dados Processados

* **`dados_tratados_ana_carnaubal_completo2.csv`**
    * **Descrição:** O dataset mestre, limpo e unificado, pronto para o treinamento do modelo de Machine Learning. Resulta da junção dos arquivos de volume e clima.

| Nome da Coluna | Tipo de Dado | Descrição |
| :--- | :--- | :--- |
| **data** | `datetime64[ns]` | Data da medição, usada como chave para a união. |
| **volume** | `float64` | Volume total do reservatório naquele dia, em hectômetros cúbicos (hm³). |
| **PRECIPITACAO...** | `float64` | Precipitação total diária em milímetros (mm). *(Liste os nomes exatos das suas colunas de clima)*. |
| **RADIACAO GLOBAL...**| `float64` | Radiação solar global acumulada no dia em Kj/m². *...* |
| **TEMPERATURA...** | `float64` | Temperatura média/máx/min do ar em Graus Celsius (°C). *...* |
| **UMIDADE...** | `float64` | Umidade relativa do ar em porcentagem (%). *...* |
| **VENTO...** | `float64` | Velocidade média do vento em metros por segundo (m/s). *...* |
| **variacao_volume** | `float64` | **A VARIÁVEL ALVO.** Calculada como `volume_hoje - volume_ontem`. Representa a perda ou ganho de volume em hm³ de um dia para o outro. |

---
## English Version

# Data Dictionary

This document describes the DataFrames created and used in the "Sentinel Flow" project.

---

## 1. Raw Data

* **`dados_tratados_ana_carnaubal.csv`**
    * **Description:** Historical time series of the daily volume of the Carnaubal Reservoir, extracted from the SAR/ANA portal and processed from the original JSON file.
    * **Columns:**
        * `data` (datetime): Measurement date in YYYY-MM-DD format.
        * `volume` (float): Reservoir volume in cubic hectometers (hm³).

* **`clima.csv`**
    * **Description:** Historical time series of meteorological data from the INMET station closest to the Carnaubal Reservoir (Crateús).
    * **Columns:** Contains various climate variables, such as `PRECIPITATION`, `GLOBAL RADIATION`, `TEMPERATURE`, etc.

---

## 2. Processed Data

* **`dados_tratados_ana_carnaubal_completo2.csv`**
    * **Description:** The master dataset, cleaned and unified, ready for training the Machine Learning model. It results from the merging of the volume and climate files.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| **data** | `datetime64[ns]` | Measurement date, used as the key for the merge. |
| **volume** | `float64` | Total reservoir volume on that day, in cubic hectometers (hm³). |
| **PRECIPITACAO...** | `float64` | Total daily precipitation in millimeters (mm). *(List the exact names of your climate columns)*. |
| **RADIACAO GLOBAL...**| `float64` | Accumulated global solar radiation for the day in Kj/m². *...* |
| **TEMPERATURA...** | `float64` | Average/max/min air temperature in Degrees Celsius (°C). *...* |
| **UMIDADE...** | `float64` | Relative air humidity in percentage (%). *...* |
| **VENTO...** | `float64` | Average wind speed in meters per second (m/s). *...* |
| **variacao_volume** | `float64` | **THE TARGET VARIABLE.** Calculated as `volume_today - volume_yesterday`. It represents the loss or gain in volume (in hm³) from one day to the next. |
