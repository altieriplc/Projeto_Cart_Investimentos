import pandas as pd

planilha = pd.ExcelFile(
    'https://raw.githubusercontent.com/altieriplc/Projeto_Cart_Investimentos/main/Dados_Base_Cart_Inv_Realizado%20-%20Portf.xlsx'
)


abas = planilha.sheet_names  # variável para somente "imprimir" os nomes das abas
#print(abas)


realizado2024 = 'Caixa Resultado 24'  # variável para associar a aba especifica dentro do arq excel


dados_caixa_2024_df = pd.read_excel(
    'https://raw.githubusercontent.com/altieriplc/Projeto_Cart_Investimentos/main/Dados_Base_Cart_Inv_Realizado%20-%20Portf.xlsx',
    sheet_name='Caixa Resultado 24').fillna(0)
# lendo a planilha e armazenando em um dataframe
#.fillna(0): Este método do pandas preenche todas as células que contêm valores NaN


dados_caixa_2024_df = dados_caixa_2024_df.rename(
    columns={'Unnamed: 0': 'Ativos'})  #renomeando coluna


dados_caixa_2024_df.loc[~dados_caixa_2024_df.index.isin([0, 2, 9, 18, 26, 27]),
                        'Ativos'] = dados_caixa_2024_df['Ativos'].str[5:]
"""
Remove os primeiros 5 caracteres de algumas linhas da coluna "Ativos"

Código:
~ -> inverte a série booleana, para selecionar índices que não estão na lisata
.str[5:] -> cria uma nova série de strings que começa a partir do 6º caractere

"""


dados_caixa_2024_df.drop(1, inplace=True)
# remove a linha especificada (linha com índice 1) do DataFrame
# inplace=True é utilizado em operações que alteram o próprio DataFrame ou Series, em vez de retornar uma nova cópia modificada
#não é necessário atribuir o resultado a uma nova variável


dados_caixa_2024_df['Média'] = (dados_caixa_2024_df.sum(
    axis=1, numeric_only=True)/12).round(2)
# calcula a média dos 12 meses


dados_caixa_2024_df['Total Anual'] = dados_caixa_2024_df.drop(columns=['Média']).sum(
    axis=1, numeric_only=True).round(2)
# calcula a soma total dos 12 meses


# ---------------------------- inserção de linhas ---------------------------- #
# criando linhas
linha_cdb = pd.DataFrame([
    ['CDB'] + [0] * (len(dados_caixa_2024_df.columns) - 1)], columns=dados_caixa_2024_df.columns)

# insere novas linhas
dados_caixa_2024_df = pd.concat([
    dados_caixa_2024_df.iloc[:3],  # Parte antes da inserção
    linha_cdb,                     # Linha nova
    dados_caixa_2024_df.iloc[3:]   # Parte depois da inserção
], ignore_index=True)
# ---------------------------- inserção de linhas ---------------------------- #


# -------------------------------- soma linhas ------------------------------- #
soma_linhas = dados_caixa_2024_df.iloc[[2, 4, 6, 7, 8]].sum()
dados_caixa_2024_df.loc[3] = ['CDB'] + soma_linhas[1:].tolist()
#é usado para converter uma série ou uma coluna de um DataFrame em uma lista Python
# -------------------------------- soma linhas ------------------------------- #


# ------------------------------ exclusão linhas ----------------------------- #
dados_caixa_2024_df = dados_caixa_2024_df.drop([2, 4, 6, 7, 8], axis=0)
# ------------------------------ exclusão linhas ----------------------------- #


# ------------------------------ renomeando colunas ----------------------------- #
dados_caixa_2024_df.at[1,'Ativos'] = 'Total Renda Fixa' # alteração do nome
dados_caixa_2024_df.at[0,'Ativos'] = 'Total Geral Mensal'
dados_caixa_2024_df.at[5,'Ativos'] = 'Outros Renda Fixa'

dados_caixa_2024_df.loc[[9, 18], 'Ativos'] = ["Total Fii's", "Total Div Ações"] # altera mais de um nome de uma vez
dados_caixa_2024_df.loc[[26, 27], 'Ativos'] = ['Total Crypto', 'Bitcoin']
# ------------------------------ renomeando colunas ----------------------------- #


# ------------------------------------- inserção coluna novos valores ------------------------------------ #
dados_caixa_2024_df['Preço Médio Pago'] = None
dados_caixa_2024_df.loc[[10, 11,12, 13, 14, 15, 16, 17],'Preço Médio Pago'] = [205.20, 3351.60, 3227.14, 3219.44, 2995.30, 3043.30, 3042.39, 3018.54]
# ------------------------------------- inserção coluna novos valores ---------------------------- #


dados_caixa_2024_df = dados_caixa_2024_df.reset_index(drop=True)# reiniciando indices


# ---------------------------- inserção de linhas ---------------------------- #
linha_vsho11 = pd.DataFrame([
    ['VSHO11'] + [0] * (len(dados_caixa_2024_df.columns) - 1)], columns=dados_caixa_2024_df.columns)
#print(linha_vsho11)

dados_caixa_2024_df = pd.concat([
    dados_caixa_2024_df.iloc[:13],  # Parte antes da inserção
    linha_vsho11,                     # Linha nova
    dados_caixa_2024_df.iloc[13:]   # Parte depois da inserção
], ignore_index=True)
# ---------------------------- inserção de linhas ---------------------------- #


dados_caixa_2024_df = dados_caixa_2024_df.drop([0, 1, 4, 14, 22], axis=0) # exclusão de mais linhas com nova numeração de indices


dados_caixa_2024_df = dados_caixa_2024_df.reset_index(drop=True)# reiniciando indices


#print(len(dados_caixa_2024_df))
print(dados_caixa_2024_df)

# ------------------------------------- Exportação GITHUB ------------------------------------ #

caminho_arquivo = r'C:\Users\altie\OneDrive\Altieri\Softwares\Dev\Projetos Pessoais\Projeto_Carteira_Investimento\dados_realiz-2024_tratados.xlsx'

dados_caixa_2024_df.to_excel(caminho_arquivo, index=False)

# ------------------------------------- Exportação GITHUB ------------------------------------ #

# inplace determina se a operação deve ser realizada no proprio Datafram

#dados_caixa_2024_df.to_excel('C:/Users/altie/OneDrive/Altieri/Softwares/Dev/Projetos Pessoais/Python/ Realizado - Alterado.xlsx',index=False) # O parâmetro index=False é usado na função to_excel para indicar que você não deseja incluir o índice do DataFrame como uma coluna adicional no arquivo Excel exportado

#dados_caixa_2024_df['Soma Total'] = dados_caixa_2024_df['Jan'] + dados_caixa_2024_df['Fev']
# soma de colunas especificas

#dados_caixa_2024_df['Soma Total'] = dados_caixa_2024_df.loc[:, 'Jan':'Dez'].sum(axis=1)
# soma determinando intervalo de colunas

#print(dados_caixa_2024_df)


