import pandas as pd
import json as js
import numpy as np

with open('dados_brutos_ana_carnaubal.json', 'r', encoding='utf-8') as file:
    dados_js = js.load(file)
    
listaano = dados_js['listaAno']
series = ['serie1', 'serie2', 'serie3', 'serie4', 'serie5']
df = []

for ano,s in zip(listaano, series):
    dados_ano = dados_js[s]
    for registro_diario in dados_ano:
        data_p = registro_diario['data']
        data_f = f'{data_p}-{ano}'
        volume_text = registro_diario['volume']
        if volume_text == 'NaN':
            volume_float = np.nan
        else:
            volume_float = float(volume_text)
        df.append({'data': data_f, 'volume': volume_float})
    
df_final = pd.DataFrame(df)
df_final.to_csv('dados_tratados_ana_carnaubal.csv', index=False)
        
