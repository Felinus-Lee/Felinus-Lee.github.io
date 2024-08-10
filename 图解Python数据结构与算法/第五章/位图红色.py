from PIL import Image

# 创建一个红色的位图（100x100像素）
bitmap_image = Image.new('RGB', (100, 100), color=(255, 0, 0))

# 保存位图
bitmap_image.save('red_bitmap.jpg')

# 显示位图
bitmap_image.show()
