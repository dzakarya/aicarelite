import tensorflow as tf
from tensorflow.keras.models import load_model
loaded = load_model('resnetapd.h5')
converter = tf.lite.TFLiteConverter.from_keras_model(loaded)
converter.inference_input_type = tf.uint8
converter.inference_output_type = tf.uint8
tfmodel = converter.convert()
open("resnetapd.tflite","wb").write(tfmodel)