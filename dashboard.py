#pip install dash
#pip install pandas
#pip install openpyxl

#layout = tudo que vais er visualizado
#callback = funcionalidades que voce tera no dashboard

#dash.plotly.com/layout

import pandas as pd 
from dash import Dash, html, dcc, Output, Input
import plotly.express as px

app = Dash(__name__)

df = pd.read_excel("Vendas.xlsx")
#lendo o arquivo excel

fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
#eixo x oridutos / quantidade eixo y / separando as lojas por id e cores diferentes / barras agrupadas

opcaoes = list(df['ID Loja'].unique())
#criando um filtro por loja

opcaoes.append("Todas as Lojas")
#adiciona a opcao todas ao final da lista

app.layout = html.Div(children=[ 
    html.H1(children="Faturamento das Lojas"),#definindo titulo principal
    html.H2(children="Grafico com faturamento de todos os produtos separados por lojas"),#Titulo secundario
    dcc.Dropdown(opcaoes, value="Todas as Lojas", id="lista_lojas"),
    dcc.Graph(
        id="grafico_quantidade_produto", #definindo nome do grafico
        figure=fig
        )
])

@app.callback(
    Output('grafico_quantidade_produto', 'figure'), #chamando o grafico e a figura do grafico
    Input('lista_lojas', 'value')
) # callback funcionalidade para atualizar o grafico conforme o filtro 


#função do update para atualizar o grafico
def update_output(value):

    #varificando se o valor do input é todos 
    if value == 'Todas as Lojas':
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group" )
    else:
        tabela_filtrada = df.loc[df['ID Loja'] == value, :]
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")

    return fig

if __name__ == '__main__':
    app.run(debug=True)