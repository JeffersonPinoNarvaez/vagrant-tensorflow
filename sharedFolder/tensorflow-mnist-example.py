#This code is an example of a simple Convolutional Neural Network (CNN) 
#implemented using TensorFlow's Keras API 
#to classify handwritten digits from the MNIST dataset.

import tensorflow.keras.layers as LK
import tensorflow.keras.models as MK
import tensorflow.keras as keras
import numpy as np

inputData = LK.Input(shape=(28,28,1))
conv1 = LK.Conv2D(8,(5,5), padding = 'valid', activation = 'sigmoid')(inputData)
pool1 = LK.MaxPool2D((2,2),(2,2))(conv1)

conv2 = LK.Conv2D(16,(5,5), padding = 'valid', activation = 'sigmoid')(pool1)
pool2 = LK.MaxPool2D((2,2),(2,2))(conv2)

flat = LK.Flatten()(pool2)
FC1 = LK.Dense(120, activation='sigmoid')(flat)
FC2 = LK.Dense(84, activation='sigmoid')(FC1)

outputData = LK.Dense(10, activation='softmax')(FC2)
model = MK.Model(inputData, outputData)
model.summary()

mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print((x_train.shape))
print((x_test.shape))

x_train = (x_train - x_train.min()) /  (x_train.max() - x_train.min())
x_test = (x_test - x_train.min()) /  (x_train.max() - x_train.min())

x_train = np.expand_dims(x_train, axis = -1)
x_test = np.expand_dims(x_test, axis = -1)

print("printing training set...")
print((x_train.shape))
print("printing testing set...")
print((x_test.shape))

history= model.compile(optimizer="adam", loss = "sparse_categorical_crossentropy", metrics = ['accuracy'])
history = model.fit(x_train, y_train, epochs= 7, batch_size = 128, validation_data=(x_test, y_test), verbose = 1)
prediction = model.predict(x_test)

print("printing prediction set...")
print(prediction.argmax(1))