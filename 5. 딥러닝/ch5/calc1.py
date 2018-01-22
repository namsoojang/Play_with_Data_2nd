# TensorFlow 추출하기 --- (※1)
import tensorflow as tf
# 상수 정의 --- (※2)
a = tf.constant(1234)
b = tf.constant(5000)
# 계산 정의 --- (※3)
add_op = a + b
# 세션 시작하기 --- (※4)
sess = tf.Session()
res = sess.run(add_op) # 식 평가하기
print(res)