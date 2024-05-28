import cv2
import numpy as np
import tensorflow
from tensorflow.keras.models import load_model

model = load_model('fd_model.h5')

def predict_from_camera(image_path):
    img = cv2.imread(image_path)
    input_img = cv2.resize(img, (48, 48))
    input_img = input_img.astype('float32') / 255
    input_img = np.expand_dims(input_img, axis=0)

    prediction = model.predict(input_img)

    # Print prediction
    print('Prediction:', prediction)

