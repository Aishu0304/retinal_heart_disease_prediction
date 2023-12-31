# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r4wGBKEd7wAL2IWKpibPBTfQrSeFUNvO
"""

import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Load a pre-trained CNN model (e.g., VGG16)
base_model = tf.keras.applications.VGG16(weights='imagenet', include_top=False)
model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Load your retina image for prediction
image_path = '/content/1343_left.jpeg'  # Replace with the path to your image
img = image.load_img(image_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = tf.keras.applications.vgg16.preprocess_input(x)

# Make the prediction
prediction = model.predict(x)

# Interpret the prediction
if prediction[0][0] > 0.5:
    print("High risk of heart attack")
else:
    print("Low risk of heart attack")