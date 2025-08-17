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
