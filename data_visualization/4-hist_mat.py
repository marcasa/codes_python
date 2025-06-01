import matplotlib.pyplot as plt
import numpy as np
pontuacoes = np.random.randint(50, 100, 100)

#print(pontuacoes)


plt.figure(figsize=(8, 5))
plt.hist(
    pontuacoes,
    bins=10,
    color='blue',
    edgecolor='black',
    #linewidth=1
)


plt.xlabel('Pontuação')
plt.ylabel('Frequência')
plt.title('Distribuição de Pontuações')
plt.show()