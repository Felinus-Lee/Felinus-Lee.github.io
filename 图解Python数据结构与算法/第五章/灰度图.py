from PIL import Image

# 创建一个灰度图（100x100像素）
gray_image = Image.new('L', (100, 100), color=127)

# 保存灰度图
gray_image.save('gray_image.jpg')

# 显示灰度图
gray_image.show()