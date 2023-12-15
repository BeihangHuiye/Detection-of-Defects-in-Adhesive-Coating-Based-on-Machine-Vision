import tensorflow as tf
from tensorflow.keras.applications.vgg19 import VGG19
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg19 import preprocess_input
import numpy as np
import cv2

# 加载VGG16模型（不包括顶层分类器）
base_model = VGG19(weights='imagenet', include_top=False)
# 定义输入张量的形状
input_shape = (256, 256, 3)  # VGG16接受3通道的图像，所以将灰度图转换为RGB图像

# 加载灰度图像并转换为RGB图像
img_path = '20_5_1_16.jpg'  # 替换为你的图像路径
img_gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
img_rgb = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2RGB)
img = cv2.resize(img_rgb, (input_shape[0], input_shape[1]))


# 将图像转换为数组并扩展维度
x = np.expand_dims(img, axis=0)
x = preprocess_input(x)

# 获取VGG16模型的某一层的输出
layer_name = 'block5_pool'
intermediate_layer_model = tf.keras.Model(inputs=base_model.input,
                                          outputs=base_model.get_layer(layer_name).output)

# 获取类映射激活的输出
features = intermediate_layer_model.predict(x)

# 将输出转换为灰度图像
class_activation_map = np.mean(features, axis=-1)
class_activation_map = np.maximum(class_activation_map, 0)  # 取正值
# #############
# 可选步骤：将类映射激活可视化
import matplotlib.pyplot as plt
plt.imshow(class_activation_map[0], cmap='jet')
plt.xticks([])  #去掉横坐标值
plt.yticks([])  #去掉纵坐标值
plt.show()
