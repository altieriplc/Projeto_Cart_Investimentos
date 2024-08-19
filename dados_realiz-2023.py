import pandas as pd

planilha = pd.ExcelFile(
    'https://raw.githubusercontent.com/altieriplc/Projeto_Cart_Investimentos/main/Dados_Cart_Inv_Realizado%20-%20Portf.xlsx'
)

abas = planilha.sheet_names

realizado2023 = 'Caixa Resultado 23'

dados_caixa_2023_df = pd.read_excel('https://raw.githubusercontent.com/altieriplc/Projeto_Cart_Investimentos/main/Dados_Cart_Inv_Realizado%20-%20Portf.xlsx', sheet_name='Caixa Resultado 23').fillna(0)

dados_caixa_2023_df.drop(1, inplace=True)


# renomeia uma coluna
dados_caixa_2023_df = dados_caixa_2023_df.rename(columns={'Unnamed: 0': 'Ativos'})


# renomeia diversas linhas
dados_caixa_2023_df.loc[[0, 2, 4, 5, 14],'Ativos'] = [
    'Total Geral Mensal', 
    'Total Renda Fixa',
    'Outros Renda Fixa',
    "Total Fii's",
    'Total Div Ações'
    ]

# remove primeiros 5 caracteres das palavras
dados_caixa_2023_df.loc[~dados_caixa_2023_df.index.isin([0, 2, 4, 5, 14]),'Ativos'] = dados_caixa_2023_df['Ativos'].str[5:]

# cria coluna média
dados_caixa_2023_df['Média'] = (dados_caixa_2023_df.sum(axis=1, numeric_only=True)/12).round(2)

# cria meses faltando
dados_caixa_2023_df['Jan'] = 0.00
dados_caixa_2023_df['Fev'] = 0.00
dados_caixa_2023_df['Mar'] = 0.00

# cria as duas novas linhas
novas_linhas = pd.DataFrame([
    ['Total Crypto'] + [0] * (len(dados_caixa_2023_df.columns) - 1),
    ['Bitcoin'] + [0] * (len(dados_caixa_2023_df.columns) - 1)
], columns=dados_caixa_2023_df.columns)

# Concatena as novas linhas ao DataFrame original
dados_caixa_2023_df = pd.concat([dados_caixa_2023_df, novas_linhas], ignore_index=True)

# renomeia uma coluna
dados_caixa_2023_df = dados_caixa_2023_df.rename(columns={'Anual': 'Total Anual'})

# reorganiza a ordem das colunas
dados_caixa_2023_df = dados_caixa_2023_df[['Ativos', 'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez', 'Média', 'Total Anual']]

# exclui a coluna total anual, pois era composta por valores
dados_caixa_2023_df = dados_caixa_2023_df.drop(columns=['Total Anual'])

# cria uma nova coluna total anual com condicionais de soma, caso existam alterações futuras
dados_caixa_2023_df['Total Anual'] = dados_caixa_2023_df.drop(columns=['Média']).sum(
    axis=1, numeric_only=True).round(2)

#localiza as linhas desejadas
#agrupa_renda_fixa = dados_caixa_2023_df.loc[[2, 3]].sum()



# ------------------------------------- Exportação GITHUB ------------------------------------ #
# r é para que o python entenda as barras invertidas no caminho
caminho_arquivo = r'C:\Users\altie\OneDrive\Altieri\Softwares\Dev\Projetos Pessoais\Projeto_Carteira_Investimento\dados_realiz-2023_tratados.xlsx'

# index false para o indice não ser exportado
dados_caixa_2023_df.to_excel(caminho_arquivo, index=False)
#print(dados_caixa_2023_df['Anual'])
# ------------------------------------- Exportação GITHUB ------------------------------------ #

print(dados_caixa_2023_df)
