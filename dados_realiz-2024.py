import pandas as pd
from pprint import pprint

planilha = pd.ExcelFile(
    'https://raw.githubusercontent.com/altieriplc/Projeto_Cart_Investimentos/main/Dados_Cart_Inv_Realizado%20-%20Portf.xlsx'
)
# O uso de "raw" (bruto) é necessário ao acessar arquivos diretamente do GitHub porque essa URL fornece o conteúdo real do arquivo sem o HTML

abas = planilha.sheet_names  # variável para somente imprimir os nomes das abas
print(abas)

realizado2024 = 'Caixa Resultado 24'  # variável para associar a aba especifica dentro do arq excel
print(realizado2024)  # imprime somento o nome da aba

dados_caixa_2024_df = pd.read_excel(
    'https://raw.githubusercontent.com/altieriplc/Projeto_Cart_Investimentos/main/Dados_Cart_Inv_Realizado%20-%20Portf.xlsx',
    sheet_name='Caixa Resultado 24').fillna(0)
#.fillna(0): Este método do pandas preenche todas as células que contêm valores NaN

pprint(dados_caixa_2024_df)

#dados_caixa_2024_df.drop(1, inplace=True)
# remove a linha especificada (linha com índice 1) do DataFrame
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
