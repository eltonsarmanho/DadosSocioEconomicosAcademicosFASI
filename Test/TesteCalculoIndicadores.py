import sys
import os
import pandas as pd

# Get the absolute path of the current script file
current_script_path = os.path.abspath(__file__)
# Get the directory containing the current script (Test/)
current_script_dir = os.path.dirname(current_script_path)
# Get the parent directory of the script's directory (DadosSocioEconomicosAcademicosFASI/)
project_root = os.path.dirname(current_script_dir)
# Add the project root to the Python path so 'Code' module can be found
sys.path.insert(0, project_root)

from Code import CalculoIndicadores
conceito_to_valor = {
        'E': 10.00,
        'B': 7.50,
        'R': 5.00,
        'I': 2.50,
        'O': 0.00  # Outros conceitos
    }
polos = ['Cameta','Limoeiro','Oeiras']
list_of_crg_dfs = []
list_of_crpl_dfs = []
for polo in polos:
    df_dados = pd.read_csv('Data/dados_hist_pdfs_' + polo + '.csv') 
    #print(df_dados.info())  
    # Crie um mapeamento dos conceitos para valores numéricos
    
    # ADD uma coluna com os valores numéricos correspondentes aos conceitos 
    df_dados['VNC'] = df_dados['Média'].map(conceito_to_valor)
    df_dados['Período Letivo'] = df_dados['Ano/Período Letivo'].astype(str)
    #print(df.head())    

    
    dt_crpl = CalculoIndicadores._get_dataframe_crpl(df_dados)
    dt_crpl['Polo'] = polo
    list_of_crpl_dfs.append(dt_crpl)

    dt_crg = CalculoIndicadores._get_dataframe_crg(df_dados)
    dt_crg['Polo'] = polo
    list_of_crg_dfs.append(dt_crg)

# Concatenate all DataFrames in the lists

df_crpl_geral = pd.concat(list_of_crpl_dfs, ignore_index=True) if list_of_crpl_dfs else pd.DataFrame()
df_crg_geral = pd.concat(list_of_crg_dfs, ignore_index=True) if list_of_crg_dfs else pd.DataFrame()

df_crg_geral.to_csv('Data/crg_geral.csv', index=False)
df_crpl_geral.to_csv('Data/crpl_geral.csv', index=False)