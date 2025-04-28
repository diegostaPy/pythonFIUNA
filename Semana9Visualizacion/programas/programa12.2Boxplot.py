import numpy as np
import matplotlib.pyplot as plt

#Generamos listas con distribución normal (con distintas desviaciones estándar)
data = [np.random.normal(0, std, 100) for std in range(1, 4)]
print(len(data))
# box plot rectangular
plt.boxplot(data,vert=True,patch_artist=True)

# Mostrar la imagen
plt.show()
