…

# Librería necesaria para utilizar la métrica Accuracy
from sklearn.metrics import accuracy_score

…

accuracy = accuracy_score(y_test, yhat_classes)

print('Accuracy - (tp + tn) / (p + n): \t%f' % accuracy)

…
