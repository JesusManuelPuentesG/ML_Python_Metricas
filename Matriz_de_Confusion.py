…
# Librería necesaria para utilizar la matriz de confusión
from sklearn.metrics import confusion_matrix
…
matrix = confusion_matrix(y_test, yhat_classes)
print()
print('Matriz de Confusión: ')
print()
print(matrix)
…