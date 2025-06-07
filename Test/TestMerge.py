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


# ===================================================================
# ===== INÍCIO DA SEÇÃO ADICIONADA: FUNÇÃO PARA RENOMEAR COLUNAS =====
# ===================================================================

def renomear_colunas_socioeconomicas(df):
    """
    Recebe um DataFrame e retorna o DataFrame com as colunas 
    socioeconômicas renomeadas para nomes mais curtos e claros.
    """
    mapa_nomes = {
        'Qual sua idade ? ': 'Idade',
        'Qual seu gênero ?': 'Genero',
        'Qual a sua cor ?': 'Cor',
        'Qua nível de escolaridade da sua mãe ?': 'Escolaridade_Mae',
        'Qual nível de escolaridade do seu pai ': 'Escolaridade_Pai',
        'Qual tipo de escola de ensino você frequentou no ensino médio ?': 'Tipo_Escola_Ensino_Medio',
        
        # Colunas do período 2024.2
        'Qual a renda familiar mensal total no período 2024.2 ?': 'Renda_Familiar_2024_2',
        'Onde você morava no período 2024.2 ?': 'Moradia_2024_2',
        'Quantas pessoas moravam na sua residência  no período 2024.2 ?\n': 'Pessoas_Residencia_2024_2',
        'Como você se desloca para a universidade no período 2024.2?': 'Transporte_2024_2',
        'Você tinha acesso a internet onde você morava no período 2024.2 ?': 'Acesso_Internet_2024_2',
        'No período 2024.2  você tinha computador próprio para estudar ?': 'Possui_Computador_2024_2',
        'Você trabalhava no período 2024.2 ?': 'Trabalhava_2024_2',
        'Quantas horas você trabalhava \nno período 2024.2 ?': 'Horas_Trabalho_2024_2',
        'Seu trabalho interferia no seu desempenho acadêmico no período 2024.2 ?': 'Trabalho_Interfere_2024_2',
        'Você recebeu auxílio financeiro da universidade  no período 2024.2 ?': 'Recebeu_Auxilio_2024_2',
        'Você já pensou em desistir da universidade  no período 2024.2 por dificuldades financeiras ?': 'Pensou_Desistir_2024_2',
        
        # Colunas do período 2024.4 (e outros períodos que possam existir)
        'Qual a renda familiar mensal total no período 2024.4 ?': 'Renda_Familiar_2024_4',
        'Onde você morava no período 2024.4 ?': 'Moradia_2024_4',
        'Quantas pessoas moravam na sua residência  no período 2024.4 ?\n': 'Pessoas_Residencia_2024_4',
        'Como você se desloca para a universidade no período 2024.4 ?': 'Transporte_2024_4',
        'Você tinha acesso a internet onde você morava no período 2024.4 ?': 'Acesso_Internet_2024_4',
        'No período 2024.4  você tinha computador próprio para estudar ?': 'Possui_Computador_2024_4',
        'Você trabalhava no período 2024.4 ?': 'Trabalhava_2024_4',
        'Quantas horas você trabalhava no período 2024.4 ?': 'Horas_Trabalho_2024_4',
        'Seu trabalho interferia no seu desempenho acadêmico no período 2024.4 ?': 'Trabalho_Interfere_2024_4',
        'Você recebeu auxílio financeiro da universidade  no período 2024.4 ?': 'Recebeu_Auxilio_2024_4',
        'Você já pensou em desistir da universidade  no período 2024.4 por dificuldades financeiras ?': 'Pensou_Desistir_2024_4',
        
        # Padronizando colunas acadêmicas
        'Período Letivo': 'Periodo_Letivo'
    }
    
    # O parâmetro errors='ignore' garante que, se uma coluna do mapa não for encontrada no df, o código não quebra.
    return df.rename(columns=mapa_nomes, errors='ignore')

# ===================================================================
# ===== FIM DA SEÇÃO ADICIONADA =====================================
# ===================================================================


# Leitura dos dados originais
df_socio_economico = pd.read_csv('Data/dados_socioEco_geral.csv')
df_academico = pd.read_csv('Data/crg_geral.csv')
df_academico_crpl = pd.read_csv('Data/crpl_geral.csv')

# Conversão de tipos
df_academico['Matricula'] = df_academico['Matricula'].astype(str)
df_academico_crpl['Matricula'] = df_academico_crpl['Matricula'].astype(str)
df_socio_economico['Matricula'] = df_socio_economico['Matricula'].astype(str)

# Merge dos DataFrames
merged_df = pd.merge(df_socio_economico, df_academico, on='Matricula')
merged_df_crpl = pd.merge(df_socio_economico, df_academico_crpl, on='Matricula')

# Remoção de colunas indesejadas
merged_df.drop(columns=['Carimbo de data/hora'], inplace=True, errors='ignore')
merged_df_crpl.drop(columns=['Carimbo de data/hora'], inplace=True, errors='ignore')


# ===================================================================
# ===== INÍCIO DA SEÇÃO ADICIONADA: CHAMADA DA FUNÇÃO DE RENOMEAÇÃO ==
# ===================================================================

print("Renomeando colunas dos DataFrames merged...")
merged_df = renomear_colunas_socioeconomicas(merged_df)
merged_df_crpl = renomear_colunas_socioeconomicas(merged_df_crpl)

print("Novas colunas do merged_df (CRG):", merged_df.columns.tolist())
print("Novas colunas do merged_df_crpl (CRPL):", merged_df_crpl.columns.tolist())

# ===================================================================
# ===== FIM DA SEÇÃO ADICIONADA =====================================
# ===================================================================


# Salvando os DataFrames com as colunas já renomeadas
print("\nSalvando os novos arquivos CSV...")
merged_df.to_csv('Data/merged_data_crg.csv', index=False)
merged_df_crpl.to_csv('Data/merged_data_crpl.csv', index=False)

print("Processo concluído com sucesso!")