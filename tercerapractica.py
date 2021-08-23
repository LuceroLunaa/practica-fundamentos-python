# Librería para generar datos aleatorios
import random
import matplotlib.pyplot as plt

# Generar un número aleatorio 

print(random.randint(1,20))
print(random.randrange(10, 100, 2))

# Declara la lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Imprime la lista
print("Lista original", lista)

# Mezcla los elementos de la lista al azar
random.shuffle(lista)
# Imprime la lista mezclada
print("Lista mixeada", lista)

# Genera una gráfica de campana de GAUSS
# Genera los datos de la gráfica
campana = [random.gauss(1,0.5) for i in range(1000)]
# Arma la gráfica
plt.hist(campana, bins=15)
# Muestra la gráfica
plt.show()