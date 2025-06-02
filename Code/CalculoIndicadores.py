import math
import pandas as pd

def calcular_crpl(df, matricula, periodo):
    df_periodo = df[(df['Matricula'] == matricula) & (df['Período Letivo'] == periodo)]
    if df_periodo.empty:
        return None
    
    soma_vnc_ch = (df_periodo['VNC'] * df_periodo['CH']).sum()
    soma_ch = df_periodo['CH'].sum()
    
    if soma_ch == 0:
        return None
    
    return round(soma_vnc_ch / soma_ch, 2)


def calcular_crg(df, matricula):
    df_matricula = df[df['Matricula'] == matricula]
    if df_matricula.empty:
        return None
    
    soma_vnc_ch = (df_matricula['VNC'] * df_matricula['CH']).sum()
    soma_ch = df_matricula['CH'].sum()
    
    if soma_ch == 0:
        return None
    
    return round(soma_vnc_ch / soma_ch, 2)


def _get_dataframe_crg(df):
    # Calcular CRG para todas as matrículas únicas
    matriculas_unicas = df['Matricula'].unique()
    dados_crg = {'Matricula': [], 'CRG': []}

    for matricula in matriculas_unicas:
        crg = calcular_crg(df, matricula)
        if crg is not None:
            dados_crg['Matricula'].append(matricula)
            dados_crg['CRG'].append(crg)

    df_crg = pd.DataFrame(dados_crg)
    #print("DataFrame CRG:")
    #print(df_crg)
    return df_crg

def _get_dataframe_crpl(df):
    # Calcular CRPL para todas as matrículas únicas
    
    matriculas_unicas = df['Matricula'].unique()
    periodos_unicos = df['Período Letivo'].unique()

    dados_crpl = {'Matricula': [], 'CRPL': [], 'Período Letivo': []}


    for matricula in matriculas_unicas:
        for periodo in periodos_unicos:
            crpl = calcular_crpl(df, matricula, periodo)
            if crpl is not None:
                dados_crpl['Matricula'].append(matricula)
                dados_crpl['CRPL'].append(crpl)
                dados_crpl['Período Letivo'].append(periodo)

    df_crpl = pd.DataFrame(dados_crpl)
    #print("DataFrame CRPL:")
    #print(df_crpl)
    return df_crpl