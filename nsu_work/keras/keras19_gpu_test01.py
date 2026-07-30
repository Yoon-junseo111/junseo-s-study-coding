import tensorflow as tf
print(tf.__version__)

gpus = tf.config.experimental.list_physical_devices("GPU")
print(gpus)

if(gpus):
    print("GPU 돈다~")
else:
    print("GPU 없다~")
    
# 오른쪽 아래 py311 클릭  
# tf291gpu 클릭