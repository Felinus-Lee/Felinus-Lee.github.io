import numpy as np

# 示例的28x28像素的灰度图像数据
# 假设这是一个简化的灰度图像数据，用随机数代替实际像素值
image_data = [
    [34, 0, 67, ..., 123],   # 第一行像素
    [255, 45, 76, ..., 89],  # 第二行像素
    # ... 其他行像素
    [12, 200, 34, ..., 255]  # 第二十八行像素
]

# 将二维图像数据展开为一维数组
flattened_image = np.array(image_data).flatten()

# 打印展开后的一维数组
print("展开后的一维数组：", flattened_image)
print("一维数组的长度：", len(flattened_image))

# 计算展开后的一维数组的节点数，即神经网络的输入层节点数
input_layer_nodes = len(flattened_image)

print("输入层节点数：", input_layer_nodes)
