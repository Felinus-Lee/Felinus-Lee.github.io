import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 定义3x3的输入数据
input_data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# 将数据转换为图像并保存
plt.imshow(input_data, cmap='gray')
plt.title('Input Data as Image')
plt.colorbar()
plt.savefig('input_image.png', dpi=300)  # 保存图像时使用更高的DPI
plt.show()

# 重新加载图像并转换为数组
image_path = 'input_image.png'
image = Image.open(image_path).convert('L')  # 将图像转换为灰度
image_array = np.array(image, dtype=np.uint8)

# 设置打印选项以显示所有数组元素
np.set_printoptions(threshold=np.inf)

# 保存数组到文本文件
output_file = 'image_array.txt'
with open(output_file, 'w') as f:
    f.write("Reconstructed array from image:\n")
    f.write(np.array2string(image_array, separator=', '))

print(f"Saved reconstructed array to {output_file}")
