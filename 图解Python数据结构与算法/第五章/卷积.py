import numpy as np
import matplotlib.pyplot as plt

# 定义输入图像和卷积核
input_image = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

filter_kernel = np.array([
    [1, 0],
    [0, 1]
])

# 计算卷积
def convolve2d(image, kernel, stride=1):
    kernel_size = kernel.shape[0]
    output_size = ((image.shape[0] - kernel_size) // stride) + 1
    output = np.zeros((output_size, output_size))
    
    for y in range(0, image.shape[0] - kernel_size + 1, stride):
        for x in range(0, image.shape[1] - kernel_size + 1, stride):
            region = image[y:y+kernel_size, x:x+kernel_size]
            output[y//stride, x//stride] = np.sum(region * kernel)
    
    return output

# 可视化卷积过程
def plot_convolution(input_image, filter_kernel, output_image):
    fig, axes = plt.subplots(3, 3, figsize=(10, 10))
    
    for i in range(3):
        for j in range(3):
            axes[i, j].imshow(input_image, cmap='gray', interpolation='none')
            axes[i, j].set_xticks([])
            axes[i, j].set_yticks([])
            if i < 2 and j < 2:
                y = i * 2
                x = j * 2
                region = input_image[y:y+2, x:x+2]
                axes[i, j].imshow(region, cmap='gray', interpolation='none')
                result = np.sum(region * filter_kernel)
                axes[i, j].set_title(f"Result: {result}")
            else:
                axes[i, j].axis('off')
    
    plt.show()

# 计算卷积结果
output_image = convolve2d(input_image, filter_kernel)

# 可视化卷积过程
plot_convolution(input_image, filter_kernel, output_image)

print("卷积结果:")
print(output_image)
