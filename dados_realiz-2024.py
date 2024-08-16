import pandas as pd

planilha = pd.ExcelFile(
    'https://raw.githubusercontent.com/altieriplc/Projeto_Cart_Investimentos/main/Dados_Cart_Inv_Realizado%20-%20Portf.xlsx'
)
"""
O uso de "raw" (bruto) na URL é necessário ao acessar arquivos diretamente do GitHub.
Essa URL fornece o conteúdo real do arquivo em vez do HTML da página, permitindo que
a função pd.ExcelFile carregue o arquivo corretamente.
    """

abas = planilha.sheet_names  # variável para somente imprimir os nomes das abas
print(abas)

realizado2024 = 'Caixa Resultado 24'  # variável para associar a aba especifica dentro do arq excel
print(realizado2024)  # imprime somento o nome da aba

dados_caixa_2024_df = pd.read_excel(
    'https://raw.githubusercontent.com/altieriplc/Projeto_Cart_Investimentos/main/Dados_Cart_Inv_Realizado%20-%20Portf.xlsx',
    sheet_name='Caixa Resultado 24').fillna(0)
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
#inplace=True é utilizado em operações que alteram o próprio DataFrame ou Series, em vez de retornar uma nova cópia modificada
#não é necessário atribuir o resultado a uma nova variável

dados_caixa_2024_df['Média'] = (dados_caixa_2024_df.sum(
    axis=1, numeric_only=True)/12).round(2)
# calcula a média dos 12 meses

dados_caixa_2024_df['Total Anual'] = dados_caixa_2024_df.drop(columns=['Média']).sum(
    axis=1, numeric_only=True).round(2)
# calcula a soma total dos 12 meses

dados_caixa_2024_df.at[2,'Ativos'] = 'Total Renda Fixa' # alteração do nome
dados_caixa_2024_df.at[0,'Ativos'] = 'Total Geral Mensal'

dados_caixa_2024_df.loc[[9, 18], 'Ativos'] = ["Total Fii's", "Total Div Ações"] # altera mais de um nome de uma vez
dados_caixa_2024_df.loc[[26, 27], 'Ativos'] = ['Total Crypto', 'Bitcoin']

print(dados_caixa_2024_df)

caminho_arquivo = r'C:\Users\altie\OneDrive\Altieri\Softwares\Dev\Projetos Pessoais\Projeto_Carteira_Investimento\dados_realiz-2024_tratados.xlsx'

dados_caixa_2024_df.to_excel(caminho_arquivo, index=False)

# inplace determina se a operação deve ser realizada no proprio Datafram

#dados_caixa_2024_df.to_excel('C:/Users/altie/OneDrive/Altieri/Softwares/Dev/Projetos Pessoais/Python/ Realizado - Alterado.xlsx',index=False) # O parâmetro index=False é usado na função to_excel para indicar que você não deseja incluir o índice do DataFrame como uma coluna adicional no arquivo Excel exportado

#dados_caixa_2024_df['Soma Total'] = dados_caixa_2024_df['Jan'] + dados_caixa_2024_df['Fev']
# soma de colunas especificas

#dados_caixa_2024_df['Soma Total'] = dados_caixa_2024_df.loc[:, 'Jan':'Dez'].sum(axis=1)
# soma determinando intervalo de colunas

#print(dados_caixa_2024_df)

# quando exportar pela segunda vez o arquivo antigo automaticamente é sobreposto o arquivo antigo
# o arquivo do git hub só é alterado atravez de commit?
# tem como alterar o arquivo original se eu tiver buscando ele na pasta? ou só exportando um novo?
#commit final limpar o arquivos mas deixa um cópia pessoal salva
