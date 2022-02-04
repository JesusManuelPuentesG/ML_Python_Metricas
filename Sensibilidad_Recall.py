…

# Librería necesaria para utilizar la métrica Recall
from sklearn.metrics import recall_score

…

recall = recall_score(y_test, yhat_classes)

print('Recall - tp / (tp + fn): \t\t%f' % recall)

…
