…
# Librería necesaria para utilizar la métrica ROC AUC
from sklearn.metrics import roc_auc_score
…
auc = 0
# ROC AUC
try:
   auc = roc_auc_score(y_test, yhat_probs)
except:
    print('En este caso no se puede calcular ROC AUC - Error')

print('ROC AUC: \t\t%f' % auc)
…
