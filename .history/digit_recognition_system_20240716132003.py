# -*- coding: utf-8 -*-
"""Digit_Recognition_System.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aYOWfkaeXT_b4FtIgSnpZXerrWEUlkn1
"""

##Fetching Dataset

import tensorflow
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense,Flatten
from sklearn.datasets import fetch_openml

!pip install gradio

import gradio as gr

import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np

objects =  tf.keras.datasets.mnist
(training_images, training_labels), (test_images, test_labels) = objects.load_data()

for i in range(9):
	# define subplot
	plt.subplot(330 + 1 + i)
	# plot raw pixel data
	plt.imshow(training_images[i])

(X_train,y_train),(X_test,y_test) = keras.datasets.mnist.load_data()

X_train #3D Image 3 dimensions array matrix

X_train.shape #60000 images data 28x28 numpy array hai

X_train[0]



X_train[0].shape  #numpy array shape hai 28x28

X_train.shape
#Test mei 10000 images hai 28x28 ke

y_train #label hai harr image k andr konsa image hai

import matplotlib.pyplot as plt
plt.imshow(X_train[0])

plt.imshow(X_train[2])

#array ko 0 se 1 k bich mei lana padega kyunki jab bhi neural nw ko train karenge values jitne similar range mei rehti hai weights utni similar nikal ke aati hai aur conversion fast hota hai...

#maximum value ko 255 se div kr denge jo max rahega uska output ayega 1 ... jo min value hai 0 usko div krne se ayega 0

X_train = X_train/255
X_test = X_test/255
training_images  = training_images / 255.0
test_images = test_images / 255.0

X_train[0]

from tensorflow.keras.layers import Flatten, Dense
model = tf.keras.models.Sequential([Flatten(input_shape=(28,28)),
                                    Dense(256, activation='relu'),
                                    Dense(256, activation='relu'),
                                    Dense(128, activation='relu'),
                                    Dense(10, activation=tf.nn.softmax)])

test=test_images[0].reshape(-1,28,28)
pred=model.predict(test)
print(pred)

def predict_image(img):
  img_3d=img.reshape(-1,28,28)
  im_resize=img_3d/255.0
  prediction=model.predict(im_resize)
  pred=np.argmax(prediction)
  return pred

#keras sequential model
model = Sequential()
#keras mei flatten layer rehta hai jo higher dimension array ko flatten kr deta hai ...
model.add(Flatten(input_shape=(28,28))) #automatically converts into 1d 784 inputs
model.add(Dense(128,activation='relu')) #activation function 128
model.add(Dense(32,activation='relu'))
model.add(Dense(10,activation='softmax')) #ek se jyada nodes hai to ham softmax use karenge

model.summary() #784x128 weight + 128biases ... dense
#128 x 10 output is weights + 10 output layer , so the trainable parms hai 1L se jyda

model.compile(loss='sparse_categorical_crossentropy',optimizer='Adam', metrics=['accuracy'])  #sparse mei labels ko 1hottencode krna nhi padta 0,1,2,3,4 ... 9 whereas in khali categorical onehottencode krna padta hai
model.compile(optimizer = 'adam',
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(training_images, training_labels, epochs=10)

test=test_images[0].reshape(-1,28,28)
pred=model.predict(test)
print(pred)

#TRAINING
history=model.fit(X_train,y_train,epochs=25,validation_split=0.2)

#PREDICTIONS
y_prob = model.predict(X_test) #test image k upar ghumega aur 0 aur 1 aur 2 aur 9 ka probaibility nikal ke dega 10,000 image k liye dega

#konse index pos pe value maximum hai ham likhenge yprop
y_pred=y_prob.argmax(axis=1)

from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)

plt.plot(history.history['loss']) #jaise jaise training badh rahe waise waise loss ho rahe
plt.plot(history.history['val_loss'])

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])

plt.imshow(X_test[0])

model.predict(X_test[0].reshape(1,28,28)).argmax(axis=1)

import numpy as np
import gradio as gr

def predict_image(img):
  img_3d=img.reshape(-1,28,28)
  im_resize=img_3d/255.0
  prediction=model.predict(im_resize)
  pred=np.argmax(prediction)
  return pred


demo = gr.Interface(predict_image, gr.Image(), "label")
if __name__ == "__main__":
    demo.launch()


#iface = gr.Interface(predict_image, inputs="sketchpad", outputs="label")

#iface.launch(debug='True')