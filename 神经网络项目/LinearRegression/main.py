# coding=utf-8

import numpy as np
import tensorflow as tf

# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.3+4

# create tensorflow structure
weight = tf.Variable(tf.random_uniform([1],-0.1,0.1))
b = tf.Variable(tf.zeros([1]))

Xtr = tf.placeholder(tf.float32,(None))
# Ytr = tf.placeholder(tf.float32,(None))

Ytr = weight*Xtr+b
loss = tf.reduce_mean(tf.square(Ytr - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.3)
train = optimizer.minimize(loss)
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for idx in range(1,301):
        sess.run(train,feed_dict={Xtr:x_data})
        if idx%30 == 0:
            print(idx,sess.run([weight,b]))