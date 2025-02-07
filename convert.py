import tensorflow as tf
from keras.models import load_model

model = load_model("YOUR MODEL NAME WITH EXTENSION")

converter = tf.lite.TFLiteConverter.from_keras_model(model)

converter.optimizations = [tf.lite.Optimize.DEFAULT]

lite_model = converter.convert()

with open("lite_model.tflite", "wb") as f:
    f.write(lite_model)