import tensorflow as tf
from tensorflow.keras.models import load_model
converter = tf.lite.TFLiteConverter.from_keras_model_file('resnetapd.h5')
tfmodel = converter.convert()
open("resnetapd.tflite","wb").write(tfmodel)