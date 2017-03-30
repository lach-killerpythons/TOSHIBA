"""
HELLLOOO KERAS!!
---------------------------
Getting started with Keras
---------------------------
1) - install python 3.53 x64 (not 3.6)
2) - make sure pip3 is installed or this will not work
3) install tensorflow $:/ pip3 install --upgrade tensorflow
4) install Keras directly to %PYTHON3_ROOT%/site-packages
"""

import keras
import tensorflow as tf
hello = tf.constant('Hello Tensorflow world')
sesh = tf.Session()
print(sesh.run(hello))
a = tf.constant(100)
b = tf.constant(200)
print(sesh.run(a+b))
