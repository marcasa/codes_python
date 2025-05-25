import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/Pedidos.csv")


#Grafico1 - Quantidae de unidades vendidas por regiao
plt.figure(figsize=(8, 5))
df.groupby('Regiao')['Unidades'].sum().plot(kind='bar', color='blue')
plt.title('Unidades Vendidas por Região')
plt.xlabel('Região')
plt.ylabel('Unidades Vendidas')
plt.xticks(rotation=45)
plt.show()


#Grafico 2- Distribuição das vendas por item (Pizza)

plt.figure(figsize=(8, 5))
df['Item'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Distribuição das Vendas por Item')  
plt.axis('equal') 
plt.show()


#grafico 3 - Relação entre preço unitario e quantidade de unidades

plt.figure(figsize=(8, 5))
plt.scatter(
    df['PrecoUnidade'],
    df['Unidades'],
    color='orange'
)

plt.title('Relação Entre Preço Unitário e Quantidade de Unidades Vendidas')
plt.xlabel('Preço Unitário')
plt.ylabel('Quantidade de Unidades Vendidas')
plt.show()

#grafico 4 - QUnatidade de unidades vendidas ao longo do tempo

df['DataPedido'] = pd.to_datetime(df['DataPedido'])
plt.figure(figsize=(10 , 6))
df.groupby('DataPedido')['Unidades'].sum().plot(kind='line', marker='o', color='green')
plt.title('Quantidade de Unidades vendidas ao longo do Tempo')
plt.xlabel('Data do Pedido')
plt.ylabel('Total de unidades vendidas')
plt.grid(True)
plt.show()


#grafico 5- Quantidade de unidades vendidas por estado em cada região

pivot = df.pivot_table(
    index = 'Estado',
    columns = 'Regiao',
    values = 'Unidades',
    aggfunc = 'sum',
    fill_value=0
)

plt.figure(figsize=(10 , 5))
pivot.plot(kind='bar', stacked=True)
plt.title('Quantidade de Unidades vendidas por Estado em cada região')
plt.xlabel('Estado')
plt.ylabel('Total de Unidades vendidas')
plt.legend(title='Região', loc='upper left', bbox_to_anchor=(1.05 , 1))
plt.xticks(rotation=45)
plt.show()