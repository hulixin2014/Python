# coding=utf-8
"""
Copyright(C), HuLixin

Author:胡立新      Version:1.0       Date: 2017-11-29

Description:Construct a SVM model.Loss using svm loss and softmax loss

History:
"""

import numpy as np
import tensorflow as tf


class SVM(object):
    """
    The Learning system using linear classification,with svm loss or softmax loss
    """

    def __init__(self, learning_rate):
        """
        Constructor

        Args:
            learning_rate(float):
                the model's rate of learning
        """
        self.Xtr = tf.placeholder(tf.float32, [None, 784])
        self.Ytr = tf.placeholder(tf.float32, [None, 10])
        self.sess = None
        self.learning_rate = learning_rate
        self.predict = None
        self.loss = None
        self.train = None
        self.create_softmax_model()
        # self.create_svm_model()
        # self.create_two_layers_model()

    def add_layer(self, input, in_size, out_size, activation_function=None):
        """
        Create a learning layer
        input(tf.placeholder):
        in_size(int):
        out_size(int):
        activation_function(function):
        """
        self.Weight =0.01 * tf.Variable(tf.random_normal([in_size, out_size]))
        self.biases = tf.zeros([1, out_size])
        Wx_plus_b = tf.matmul(input, self.Weight) + self.biases
        if activation_function is None:
            return Wx_plus_b
        else:
            return activation_function(Wx_plus_b)

    def create_softmax_model(self):
        """
        Create a learning model with softmax loss
        """
        self.predict = self.add_layer(self.Xtr, 784, 10, None)
        # loss_cross_entropy = tf.reduce_mean(-tf.reduce_sum(self.Ytr * tf.log(self.predict),
        #                                                    reduction_indices=[1]))
        self.loss = tf.reduce_sum(tf.nn.softmax_cross_entropy_with_logits(labels=self.Ytr,logits=self.predict))
        optimizer = tf.train.GradientDescentOptimizer(self.learning_rate)
        self.train = optimizer.minimize(self.loss)

    def create_svm_model(self):
        """
        Create a learning model with svm loss
        """
        self.predict = self.add_layer(self.Xtr, 784, 10, tf.nn.softmax)
        # cost = ∑_(i=1)^N max⁡(1-y_i⋅(w⋅x_i+b),0)+1/2 + 0.5 * ‖w‖^2
        self.loss = tf.reduce_sum(tf.maximum(
            1 - self.Ytr * self.predict, 0))
        optimizer = tf.train.AdamOptimizer(self.learning_rate)
        self.train = optimizer.minimize(self.loss)

    def create_two_layers_model(self):
        """
        Create a learning model with two layers
        """
        layer1 = self.add_layer(self.Xtr, 784, 10, tf.nn.tanh)
        self.predict = self.add_layer(layer1,10, 10, tf.nn.softmax)
        self.loss = tf.reduce_mean(-tf.reduce_sum(self.Ytr * tf.log(self.predict),
                                                                reduction_indices=[1]))
        optimizer = tf.train.AdamOptimizer(self.learning_rate)
        self.train = optimizer.minimize(self.loss)

    def train_model(self, x_data, y_data):
        """
        Train the learning model

        Args:
            x_data(np.array):
                input data
            y_data(np.array):
                output data
        """
        init = tf.global_variables_initializer()
        self.sess = tf.Session()
        self.sess.run(init)
        for idx in range(1, 2001):
            _,loss = self.sess.run([self.train, self.loss], feed_dict={self.Xtr: x_data, self.Ytr: y_data})
            if idx%200 == 0:
                print(loss)

    def model_predict(self, x_data, y_data=None):
        """
        Use the trained model to predict data

        Args:
            x_data(np.array):
                input data
            y_data(np.array):
                output data
        Returns:
            accuracy(float):accuracy of prediction
            Ypred(np.array):result of prediction
        """
        Ypred = self.sess.run(self.predict, feed_dict={self.Xtr: x_data})
        Ypred = np.argmax(Ypred, axis=1)
        accuracy = None
        if y_data is not None:
            correct_predict = np.equal(Ypred, np.argmax(y_data, axis=1))
            accuracy = np.mean(correct_predict)
        return Ypred, accuracy

    def __del__(self):
        """
        Destructor
        """
        if self.sess is not None:
            self.sess.close()
