import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

class ModelClass():
  def _split_data(self, X, y):
    self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)
         
  def __init__(self, X, y):
    self._split_data(X, y)
    
  def trainer(self, type='desicion tree'):
    print(type, '\n')
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
  def pred(self, X_unseen):
    result_pred = self.clf.predict(X_unseen)
    return result_pred
    
  # create log for training phase
  def log(self):
    print("Confusion Matrix:\n ", confusion_matrix(self.y_test, self.y_pred))
    print("Accuracy : ", accuracy_score(self.y_test, self.y_pred)*100)
    print("Report : ", classification_report(self.y_test, self.y_pred))