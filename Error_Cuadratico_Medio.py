…

# Librería necesaria para utilizar la métrica Error Cuadrático Medio
from sklearn.metrics import mean_squared_error

…

mse = mean_squared_error(testy[:,0], ypred[:,0])

print('Error Cuadrático Medio: \t%f' % mse)

…
