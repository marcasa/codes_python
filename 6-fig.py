import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1 , 6)
y1 = np.array([3, 5, 7, 9, 11])
y2 = np.array([4, 6, 8, 10, 12])


#criando subplots 

fig, ax = plt.subplots(2, figsize=(8, 8))

ax[0].bar(x, y1, color='skyblue')
ax[0].set_title('Grafico 1')

ax[1].plot(x, y2, marker='o', color='red')
ax[1].set_title('Grafico 2')

plt.tight_layout()
plt.show()  