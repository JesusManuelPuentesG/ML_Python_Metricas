…

# Librería necesaria para utilizar la métrica Error Absoluto Medio
from sklearn.metrics import mean_absolute_error

…

mae = mean_absolute_error (testy[:,0], ypred[:,0])

print('Error Cuadrático Medio: \t%f' % mae)

…
