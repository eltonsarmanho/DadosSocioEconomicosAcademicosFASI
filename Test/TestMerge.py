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

df_socio_economico = pd.read_csv('Data/dados_socioEco_geral.csv')
df_academico = pd.read_csv('Data/crg_geral.csv')
df_academico_crpl = pd.read_csv('Data/crpl_geral.csv')

df_academico['Matricula'] = df_academico['Matricula'].astype(str)
df_academico_crpl['Matricula'] = df_academico_crpl['Matricula'].astype(str)

df_socio_economico['Matricula'] = df_socio_economico['Matricula'].astype(str)
# Merge the DataFrames on the 'Matricula' column
merged_df = pd.merge(df_socio_economico, df_academico, on='Matricula')
merged_df_crpl = pd.merge(df_socio_economico, df_academico_crpl, on='Matricula')


merged_df.drop(columns=['Carimbo de data/hora'], inplace=True)
merged_df_crpl.drop(columns=['Carimbo de data/hora'], inplace=True)


# Save the merged DataFrame to a new CSV file
merged_df.to_csv('Data/merged_data_crg.csv', index=False)
merged_df_crpl.to_csv('Data/merged_data_crpl.csv', index=False)