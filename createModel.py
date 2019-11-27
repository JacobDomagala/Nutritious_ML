import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
import pickle 

rootDir = os.path.join(os.path.curdir, "downloads")

categories = os.listdir(rootDir)
labels = dict(zip(range(0, len(categories)), categories))
numLabels = len(categories)
trainData = []

for label in categories:
    pathToData = os.path.join(rootDir, label)
    listOfImages = os.listdir(pathToData)
    currentLabel = categories.index(label)
    for image in listOfImages:
        imgBytes = cv2.imread(os.path.join(pathToData, image))
        trainData.append([imgBytes, currentLabel])

print(len(trainData))

random.shuffle(trainData)

X = []
y = []

for features, label in trainData:
    X.append(features)
    y.append(label)

# images are 128,128 for now!
X = np.array(X).reshape(-1, 128, 128, 3)
y = np.array(y)

pickle_out = open("X.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()

# pickle.in = open("X.pickle", "rb")
# X = pickle.load(pickle.in)
# pickle.in = open("y.pickle", "rb")
# y = pickle.load(pickle.in)

X = X/255.0

model = Sequential([
Conv2D(64, (3,3), activation=tf.nn.relu, input_shape = (128, 128, 3)),
MaxPooling2D(2,2),
Conv2D(64, (3,3), activation=tf.nn.relu),
MaxPooling2D(2,2),
Flatten(),
Dense(64, activation=tf.nn.relu),
Dense(numLabels, activation=tf.nn.softmax)])

model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(X, y, batch_size=32, epochs=10, validation_split=0.1)

model.save("testModel.tf")
converter = tf.lite.TFLiteConverter.from_saved_model("testModel.tf")

tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)