import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf

# 加载预训练模型
model = tf.keras.models.load_model('cnn_mnist_model.h5')

# 预处理图像函数
def preprocess_image(image):
    image = image.resize((28, 28)).convert('L')
    image = np.array(image)
    image = image.reshape(1, 28, 28, 1).astype('float32') / 255
    return image

# 预测函数
def predict_image(image):
    preprocessed_image = preprocess_image(image)
    predictions = model.predict(preprocessed_image)
    predicted_label = np.argmax(predictions)
    return predicted_label

# 加载图像函数
def load_image():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    image = Image.open(file_path)
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    canvas.image = photo
    label = predict_image(image)
    result_label.config(text=f'Predicted Label: {label}')

# 创建主窗口
root = tk.Tk()
root.title("MNIST Digit Recognizer")

# 创建Canvas来显示图像
canvas = tk.Canvas(root, width=280, height=280)
canvas.pack()

# 创建按钮来加载图像
load_button = tk.Button(root, text="Load Image", command=load_image)
load_button.pack()

# 创建标签来显示预测结果
result_label = tk.Label(root, text="Predicted Label: ")
result_label.pack()

# 运行主循环
root.mainloop()
