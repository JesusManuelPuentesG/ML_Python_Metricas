…

# Librería necesaria para utilizar la métrica Precision
from sklearn.metrics import precision_score

…

precision = precision_score(y_test, yhat_classes)

print('Precision - tp / (tp + fp): \t\t%f' % precision)

…
