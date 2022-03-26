from matplotlib.pyplot import axis
from sklearn import datasets
import numpy as np
import cv2

# create list for trainin/test data
train_features = []
train_labels = []
test_features = []
test_labels = []

# load data from csv file 
iris =datasets.load_iris()

features = iris['data']
labels = iris['target']

training_features, test_features = np.split(features, 2, axis = 0)
training_labels, test_labels = np.split(labels, 2, axis = 0)

print('train_features: ', np.shape(train_features))
print('train_labels: ', np.shape(train_labels))
print('test_features: ', np.shape(test_features))
print('test_labels: ', np.shape(test_labels))

print('train_features: ', train_features)
print('train_labels: ', train_labels)
print('test_features: ', test_features)
print('test_labels: ', test_labels)


# Create neural network
net = cv2.ml.ANN_MLP_create()
net.setLayerSizes(np.array([4,5,5,3]))
net.setTrainMethod(cv2.ml.ANN_MLP_BACKPROP)
net.setActivationFunction(cv2.ml.ANN_MLP_SIGMOID_SYM)



# Train the network
net.train(np.array(training_features, dtype = np.float32), cv2.ml.ROW_SAMPLE, np.array(training_labels, dtype = np.float32))


# Classify 
pred = net.predict(np.array(test_features, dtype = np.float32))



# Print error
error = np.mean(np.square(np.array(test_labels, dtype = np.float32) - pred[1]))
print('the error is: ', error)