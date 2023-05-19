import numpy as np
from sklearn.datasets import make_blobs
import class_model


# create random data
centers = [(-5, -5, -5), (5, 5, 5)]
cluster_std = [0.8, 1]
X, y = make_blobs(n_samples=1000, cluster_std=cluster_std, centers=centers, n_features=3, random_state=1)

X_unseen = X[900:]
X = X[:900]
y = y[:900]


# train and validation of single clf
model = ModelClass(X, y).trainer(type = 'desicion tree')

# logs of training phase
model.log()

# test of unseen data
import time
start = time.time()
model.pred(X_unseen)
end = time.time()
print((end - start)*1000, 'millisecond')