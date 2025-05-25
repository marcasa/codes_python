import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/Pedidos.csv")

fig, ax = plt.subplots(2, 2 , figsize=(15,15))

#Grafico1 - Quantidae de unidades vendidas por regiao

df.groupby('Regiao')['Unidades'].sum().plot(kind='bar', color='blue', ax=ax[0,0])
ax[0, 0].set_title('Unidades Vendidas por Região')
ax[0, 0].set_xlabel('Região')
ax[0, 0].set_ylabel('Unidades Vendidas')
ax[0, 0].tick_params(axis='x', rotation=45)


#Grafico 2- Distribuição das vendas por item (Pizza)

df['Item'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax[0 ,1])
ax[0, 1].set_title('Distribuição das Vendas por Item')  
ax[0, 1].axis('equal')


#grafico 3 - Relação entre preço unitario e quantidade de unidades


ax[1, 0].scatter(
    df['PrecoUnidade'],
    df['Unidades'],
    color='orange'
)

ax[1, 0].set_title('Relação Entre Preço Unitário e Quantidade de Unidades Vendidas')
ax[1, 0].set_xlabel('Preço Unitário')
ax[1, 0].set_ylabel('Quantidade de Unidades Vendidas')


#grafico 4 - QUnatidade de unidades vendidas ao longo do tempo

df['DataPedido'] = pd.to_datetime(df['DataPedido'])
df.groupby('DataPedido')['Unidades'].sum().plot(kind='line', marker='o', color='green', ax=ax[1,1])
ax[1, 1].set_title('Quantidade de Unidades vendidas ao longo do Tempo')
ax[1, 1].set_xlabel('Data do Pedido')
ax[1, 1].set_ylabel('Total de unidades vendidas')
ax[1, 1].grid(True)







plt.show()