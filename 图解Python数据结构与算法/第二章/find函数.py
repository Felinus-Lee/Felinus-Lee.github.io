my_string = "Hello, World!"

# 查找子字符串
index = my_string.find("World")

# 打印结果
if index != -1:
    print(f"子字符串在索引 {index} 处找到。")
else:
    print("未找到子字符串。")
