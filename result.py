import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt
X = np.loadtxt('misc.txt')
y = np.loadtxt('misclab.txt')
clf = svm.SVC(kernel='linear', C = 1.0)
clf.fit(X,y)
test=np.loadtxt('test.txt')
clf.predict(test)