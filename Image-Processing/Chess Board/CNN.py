import numpy as np
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import random


x = []
y = []

# model = tf.keras.models.Sequential()
# model.add(tf.keras.Input(shape=(2,)))
# model.add(tf.keras.layers.Dense(units=8, activation='sigmoid'))
# model.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))
# print(model.summary())

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))




class FeatureExtractor(object):
    def extract_features(self, square):
        raise NotImplementedError