…

# Librería necesaria para utilizar la métrica F1-Score
from sklearn.metrics import f1_score

…

f1 = f1_score(y_test, yhat_classes)

print('F1 score - 2 tp / (2 tp + fp + fn): \t%f' % f1)

…
