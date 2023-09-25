import tensorflow as tf
import numpy as np

a=tf.Variable(np.array(1.,2.,5.))
b=tf.Variable(np.array(5.,7.,98.,))
c=tf.dotproduct(a,b)
print(c)