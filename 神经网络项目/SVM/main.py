import tensorflow as tf
import numpy as np

from tensorflow.examples.tutorials.mnist import input_data
from SVM import SVM

# number 1 to 10 data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

Xtr,Ytr = mnist.train.next_batch(1000)
Xte,Yte = mnist.train.next_batch(50)

svm = SVM(0.2)
svm.train_model(Xtr,Ytr)
print(svm.model_predict(Xte,Yte))
print(np.argmax(Yte,axis=1))

