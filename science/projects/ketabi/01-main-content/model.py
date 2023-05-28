import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

class ModelClass():
  def __init__(self, X, y):
    X = np.array(X)
    y = np.array(y)
    self._split_data(X, y)


  def _balance_data(self, X, y):
    idx_true = list(np.where(y==1)[0])
    X_true = X[idx_true]
    y_true = y[idx_true]
    X_false = np.delete(X, idx_true, axis=0)
    y_false = np.delete(y, idx_true)
    np.random.shuffle(X_false); X_false = X_false[:len(X_true)]
    np.random.shuffle(y_false); y_false = y_false[:len(y_true)]
    X = np.vstack([X_true, X_false])
    y = np.hstack([y_true, y_false])
    return (X, y)
  
  def _split_data(self, X, y):
    X, y = self._balance_data(X, y)
    self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)
         
    
  def trainer(self, type='desicion tree'):
    if type == 'svm':
      self.clf = svm.SVC(kernel='rbf', gamma='auto')
    elif type == 'random forest':
      self.clf = RandomForestClassifier(n_estimators=5, criterion = "gini", max_depth=5, random_state=42)
    elif type == 'desicion tree':
      self.clf = DecisionTreeClassifier(criterion = "gini", random_state = 100, max_depth=3, min_samples_leaf=5)
    else:
      raise ValueError('type should be svm, random forest or decision tree')

    self.clf.fit(self.X_train, self.y_train)
    self.y_pred = self.clf.predict(self.X_test)
    return self

  # prediction attr just in test phase
  def predict(self, X_unseen=None):
    if X_unseen:
      result_pred = self.clf.predict(X_unseen)
    else: 
      result_pred = self.clf.predict(self.X_test)
    return result_pred
    
  # create log for training phase
  def report(self):
    cm = confusion_matrix(self.y_test, self.y_pred)
    acc = accuracy_score(self.y_test, self.y_pred) * 100
    report = classification_report(self.y_test, self.y_pred, output_dict=True)
    return report, acc, cm