import tensorflow as tf

print(tf.__version__)

mat1 = [0,1,2]
mat2 = [2,1,0]

with tf.device('/cpu:0'):
	tn1 = tf.placeholder(dtype= tf.int32, shape=[3])
	tn2 = tf.placeholder(dtype= tf.int32, shape=[3])
	tn3 = tn1 + tn2

with tf.Session() as sess:
	result = sess.run(tn3,{tn1:mat1,tn2:mat2})
	print(result)