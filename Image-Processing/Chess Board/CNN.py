import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from tensorflow import keras
from keras import layers
import matplotlib.pyplot as plt
from ImageHelpers import * 
import cv2
#import random

# cifar10 = keras.datasets.cifar10
# (train_images, train_labels), (test_images, test_labels) = cifar10.load_data()


train_images = []
train_labels = []
test_images = []
test_labels = []

splitBoard('newimg000.jpg','path','store',False)
name = ''

for i in range(64):
    temp = cv2.imread(name+str(i)+'.png')
    # print('shape of square: ', temp.shape)
    train_images.append(temp)
    train_labels.append(np.array(0))


splitBoard('newimgrotated000.jpg','path','store',False, 'rotated')
name = 'rotated'
for i in range(64):
    temp = cv2.imread(name+str(i)+'.png')
    # print('shape of square: ', temp.shape)
    train_images.append(temp)
    train_labels.append(np.array(0))

train_images = np.array(train_images)
train_labels = np.array(train_labels)

train_labels[:16] = np.array(np.array(2))
train_labels[16:48] = np.array(np.array(0))
train_labels[48:64] = np.array(np.array(1))
train_labels[64:80] = np.array(np.array(1))
train_labels[80:112] = np.array(np.array(0))
train_labels[112:128] = np.array(np.array(2))

test_images = train_images
test_labels = train_labels

print("the shape of trainning image: ", train_images.shape)
print("the shape of test image: ", test_images.shape)
print("the shape of trainning labels: ", train_labels.shape)
print("the shape of test labels: ", test_labels.shape)

# Normalize: 0,255 -> 0,1
train_images = train_images / 255.0  
test_images  = test_images / 255.0
#                 0        -1     +1
class_names = ['Empty', 'Black', 'White']

# model...
model = keras.models.Sequential()
model.add(layers.Conv2D(3, (3,3), strides=(1,1), padding="valid", activation='relu', input_shape=(50,50,3)))
model.add(layers.MaxPool2D((5,5)))
""" model.add(layers.Conv2D(3, 3, activation='relu'))
model.add(layers.MaxPool2D((2,2))) """

model.add(layers.Flatten())
model.add(layers.Dense(100, activation='tanh'))
model.add(layers.Dense(3,activation='tanh'))
print(model.summary())

# loss and optimizer
loss = keras.losses.SparseCategoricalCrossentropy(from_logits=True)
optim = keras.optimizers.Adam(lr=1e-4)
metrics = ["accuracy"]

model.compile(optimizer=optim, loss=loss, metrics=metrics)

# training
batch_size = 1
epochs = 64

model.fit(train_images, train_labels, epochs=epochs,
          batch_size=batch_size, verbose=2,shuffle=True)

""" model.fit(test_images, test_labels, epochs=epochs,
          batch_size=batch_size, verbose=2,shuffle=True) """


print('*********************************************************************************************')
# evaulate
model.evaluate(test_images,  test_labels, batch_size=batch_size, verbose=2)

print('*********************************************************************************************')

prediction = model.predict(test_images)
print('predictions', prediction)

predictionLabels =[]
for i in prediction:
    predictionLabels.append(class_names[list(i).index(max(list(i)))])
print("prediction labels: ",predictionLabels)