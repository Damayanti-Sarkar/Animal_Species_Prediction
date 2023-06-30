# -*- coding: utf-8 -*-
"""Animal Species Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NDcjgBHFvo8uk5AEQ15K9Hp-iqlGSb1f
"""

# Loading libraries and Packages
import numpy as np
import matplotlib.pyplot as plt
import requests

from PIL import Image
from io import BytesIO
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions

# Initialize a ResNet-50 model with pre-trained weights from ImageNet dataset.
model = ResNet50(weights = 'imagenet')

def predict_animal_species(image_path):

    # Load and preprocess the image
    img = Image.open(image_path)
    img = img.resize((224, 224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    processed_img = preprocess_input(img_array)

    # Make predictions
    predictions = model.predict(processed_img)
    decoded_predictions = decode_predictions(predictions, top=3)[0]

    # Display the predictions
    for _, animal, probability in decoded_predictions:
      print(f"{animal}: {probability: .2%}")

    #Display the image
    plt.imshow(img)
    plt.axis('off')
    plt.show()

# Loading the animal image to be predicted
image_path = '/content/animal_img2.jpg'
predict_animal_species (image_path)