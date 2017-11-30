import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
from KNN import KNN

mnist = input_data.read_data_sets("MNIST_Data/data/", one_hot=True)
Xtr, Ytr = mnist.train.next_batch(1000)
Xte, Yte = mnist.test.next_batch(200)
Ytr = np.argmax(Ytr,axis=1)
Yte = np.argmax(Yte,axis=1)

# print(type(Xtr))
# print(Xtr.shape)
#
# print(type(Ytr))
# print(Ytr.shape)
# print(Ytr[0])
# print(Ytr)

knn = KNN()
knn.train(Xtr,Ytr)
Ypre,accuracy = knn.predict(Xte,Yte,3)

print(accuracy)
print(Ypre)
print(Yte)


