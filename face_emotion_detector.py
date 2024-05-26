import cv2
import numpy as np
import tensorflow
from tensorflow.keras.models import load_model

class StandardizedConv2DWithOverride(tensorflow.keras.layers.Conv2D):
    def __init__(self, *args, **kwargs):
        super(StandardizedConv2DWithOverride, self).__init__(*args, **kwargs)

    def convolution_op(self, inputs, kernel):
        mean, var = tensorflow.nn.moments(kernel, axes=[0, 1, 2], keepdims=True)
        return tensorflow.nn.conv2d(
            inputs,
            (kernel - mean) / tensorflow.sqrt(var + 1e-10),
            padding="VALID",
            strides=list(self.strides),
            name=self.__class__.__name__,
        )

tensorflow.keras.utils.get_custom_objects()['StandardizedConv2DWithOverride'] = StandardizedConv2DWithOverride

model = load_model('fd_model.h5')

def predict_from_camera(image_path):
    img = cv2.imread(image_path)
    input_img = cv2.resize(img, (48, 48))
    input_img = input_img.astype('float32') / 255
    input_img = np.expand_dims(input_img, axis=0)

    prediction = model.predict(input_img)

    # Print prediction
    print('Prediction:', prediction)

