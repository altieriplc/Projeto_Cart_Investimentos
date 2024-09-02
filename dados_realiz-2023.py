import pandas as pd

planilha = pd.ExcelFile(
    'https://raw.githubusercontent.com/altieriplc/Projeto_Cart_Investimentos/main/Dados_Base_Cart_Inv_Realizado%20-%20Portf.xlsx'
)  #acesso direto ao arquivo no github

abas = planilha.sheet_names  # variável para somente "imprimir" os nomes das abas
#print(abas)

realizado2023 = 'Caixa Resultado 23'  # variável para associar a aba especifica dentro do arq excel

dados_caixa_2023_df = pd.read_excel(
    'https://raw.githubusercontent.com/altieriplc/Projeto_Cart_Investimentos/main/Dados_Base_Cart_Inv_Realizado%20-%20Portf.xlsx',
    sheet_name='Caixa Resultado 23').fillna(0)
# lendo a planilha e armazenando em um dataframe
#.fillna(0): Este método do pandas preenche todas as células que contêm valores NaN

dados_caixa_2023_df.drop(1, inplace=True)  # excluindo linha

# ------------------------------ renomeando colunas ----------------------------- #
dados_caixa_2023_df = dados_caixa_2023_df.rename(
    columns={'Unnamed: 0': 'Ativos'})

# renomeia diversas linhas
dados_caixa_2023_df.loc[[0, 2, 4, 5, 14], 'Ativos'] = [
    'Total Geral Mensal', 'Total Renda Fixa', 'Outros Renda Fixa',
    "Total Fii's", 'Total Div Ações'
]
# ------------------------------ renomeando colunas ----------------------------- #
dados_caixa_2023_df.loc[~dados_caixa_2023_df.index.isin([0, 2, 4, 5, 14]),
                        'Ativos'] = dados_caixa_2023_df['Ativos'].str[5:]
# remove primeiros 5 caracteres das palavras
# ------------------------------ renomeando colunas ----------------------------- #

# ---------------------------- inserção de linhas e colunas --------------------- #
dados_caixa_2023_df['Média'] = (
    dados_caixa_2023_df.sum(axis=1, numeric_only=True) / 12).round(2)
# cria coluna média

dados_caixa_2023_df['Jan'] = 0.00
dados_caixa_2023_df['Fev'] = 0.00
dados_caixa_2023_df['Mar'] = 0.00
dados_caixa_2023_df['Preço Médio Pago'] = None
dados_caixa_2023_df.loc[[5, 6, 7, 8, 9, 10, 11, 12], 'Preço Médio Pago'] = [
    205.20, 3351.60, 3227.14, 3219.44, 2995.30, 3043.30, 3042.39, 3018.54
]
# cria meses faltando

dados_caixa_2023_df['Preço Médio Pago'] = dados_caixa_2023_df[
    'Preço Médio Pago'].fillna(0)
#preenche valores vazios com zero

novas_linhas = pd.DataFrame(
    [['Total Crypto'] + [0] * (len(dados_caixa_2023_df.columns) - 1),
     ['Bitcoin'] + [0] * (len(dados_caixa_2023_df.columns) - 1)],
    columns=dados_caixa_2023_df.columns)
# cria as duas novas linhas

dados_caixa_2023_df = pd.concat([dados_caixa_2023_df, novas_linhas],
                                ignore_index=True)
# Concatena as novas linhas ao DataFrame original
# ---------------------------- inserção de linhas e colunas ----------------------- #

dados_caixa_2023_df = dados_caixa_2023_df.rename(
    columns={'Anual': 'Total Anual'})
# renomeia uma coluna

dados_caixa_2023_df = dados_caixa_2023_df.drop(columns=['Total Anual'])
# exclui a coluna total anual, pois era composta por valores

dados_caixa_2023_df = dados_caixa_2023_df.drop([0, 1, 4, 0, 13, 19], axis=0)

dados_caixa_2023_df['Total Anual'] = dados_caixa_2023_df.drop(
    columns=['Média']).sum(axis=1, numeric_only=True).round(2)
# cria uma nova coluna total anual com condicionais de soma, caso existam alterações futuras

dados_caixa_2023_df = dados_caixa_2023_df[[
    'Ativos', 'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set',
    'Out', 'Nov', 'Dez', 'Média', 'Total Anual', 'Preço Médio Pago'
]]
# reorganiza a ordem das colunas

dados_caixa_2023_df = dados_caixa_2023_df.reset_index(drop=True)# reiniciando indices

# ---------------------------- inserção de linhas ---------------------------- #
linha_vsho11 = pd.DataFrame([
    ['VSHO11'] + [0] * (len(dados_caixa_2023_df.columns) - 1)], columns=dados_caixa_2023_df.columns)
#print(linha_vsho11)

dados_caixa_2023_df = pd.concat([
    dados_caixa_2023_df.iloc[:10],  # Parte antes da inserção
    linha_vsho11,                     # Linha nova
    dados_caixa_2023_df.iloc[10:]   # Parte depois da inserção
], ignore_index=True)
# ---------------------------- inserção de linhas ---------------------------- #

# ------------------------------------- Exportação GITHUB ------------------------------------ #
# r é para que o python entenda as barras invertidas no caminho
caminho_arquivo = r'C:\Users\altie\OneDrive\Altieri\Softwares\Dev\Projetos Pessoais\Projeto_Carteira_Investimento\dados_realiz-2023_tratados.xlsx'

# index false para o indice não ser exportado
dados_caixa_2023_df.to_excel(caminho_arquivo, index=False)
#print(dados_caixa_2023_df['Anual'])
# ------------------------------------- Exportação GITHUB ------------------------------------ #

print(dados_caixa_2023_df)
