"""
Copyright(C), HuLixin

Author:胡立新      Version:1.0       Date: 2017-11-29

Description:Construct a KNN model

History:
"""

import numpy as np


class KNN(object):
    def __init__(self):
        """
        Constructor
        """
        self.__Xtr = []
        self.__Ytr = []

    def train(self, X, Y):
        """
        Train the model,just memorize the data

        Args:
            X(array):
                a set of inputs,the first dimension is the number of data
            Y(array):
                a set of outputs,the first dimension is the number of data
        """
        self.__Xtr = X
        self.__Ytr = Y

    def predict(self, X, Y=None, k=1):
        """
        Predict which class X belong to

        Args:
            X(array):
                a set of inputs,the first dimension is the number of data
            Y(array):
                a set of outputs,the first dimension is the number of data
            k(int):
                the number of points nearest from the predicted point
        Returns:
            labels(array):the classes the X belong to
            accuracy(float):prediction accuracy
        """
        predict_num = X.shape[0]
        Ypred = np.zeros(predict_num,dtype=self.__Ytr.dtype)

        # use L1 distance
        for idx in range(predict_num):
            distances = np.sum(np.abs(self.__Xtr - X[idx,:]),axis=1)
            labels = self.get_k_labels(distances,k)
            Ypred[idx] = self.most_quantity_index(labels)
        accuracy = None
        if Y is not None:
            accuracy = np.sum(Ypred==Y)/float(predict_num)
        return Ypred,accuracy


    @staticmethod
    def most_quantity_index(arr):
        """
        Get the element the number is most

        Args:
            arr(array,list):
                numpy array

        Returns:
            (int) element of array
        """
        num_dict = {}
        for elem in arr:
            if elem in num_dict:
                num_dict[elem] += 1
            else:
                num_dict[elem] = 1
        return sorted(num_dict.items(),key=lambda x:x[1],reverse=True)[0][0]

    def get_k_labels(self, distances, k):
        """
        Get k label nearest from the point

        Args:
            distances(np.array):
                distance from the point
            k(int):
                the number of labels
        Returns:
            labels(list)
        """
        labels = []
        for idx in range(k):
            min_index = np.argmin(distances)
            labels.append(self.__Ytr[min_index])
            distances[min_index] = np.inf
        return labels
