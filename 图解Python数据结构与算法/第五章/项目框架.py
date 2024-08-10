import os
import sys
import openai
from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QPixmap, Qt, QGuiApplication,QFont, QIcon
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import GraphCypherQAChain
from langchain.graphs import Neo4jGraph
from langchain.chains.question_answering import load_qa_chain
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, \
    QTextEdit, QMessageBox, QDialog, QHBoxLayout
import time


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 应用样式表
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 8px 16px;
                font-size: 12px; /* 调整字体大小 */
                font-family: "Microsoft YaHei"; /* 使用微软雅黑字体，确保字体存在 */
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QLabel {
                font-size: 14px;
                font-family: Arial;
            }
            QLineEdit, QTextEdit {
                font-size: 14px;
                font-family: Arial;
            }
            #input_textbox, #output_textbox {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 8px;
            }
            #contact_us_btn {
                background-color: #e74c3c;
            }
        """)

        # 设置窗口的大小和位置
        self.setGeometry(100, 100, 400, 500)

        # 设置窗口的标题
        self.setWindowTitle("史谈文博系统v1.0")

        # 设置窗口图标
        icon = QIcon("史谈文博icon.png")  # 用实际的图标图像路径替换 "path_to_your_icon_image.png"
        self.setWindowIcon(icon)

        # Create buttons
        self.neo4j_btn = QPushButton("Neo4j设置")
        self.model_btn = QPushButton("Model设置")

        # Create widgets for Neo4j settings
        self.neo4j_url_label = QLabel("URL:")
        self.neo4j_url_input = QLineEdit()
        self.neo4j_username_label = QLabel("Username:")
        self.neo4j_username_input = QLineEdit()
        self.neo4j_password_label = QLabel("Password:")
        self.neo4j_password_input = QLineEdit()

        # Create widget for Model settings
        self.api_label = QLabel("API:")
        self.api_input = QLineEdit()

        # Create input and output text boxes
        self.input_label = QLabel("向我提出你的问题:")
        self.input_textbox = QTextEdit()
        self.output_label = QLabel("来看看我的回答:")
        self.output_textbox = QTextEdit()

        # Create Save and Clear buttons for Neo4j settings
        self.neo4j_save_btn = QPushButton("保存")
        self.neo4j_clear_btn = QPushButton("清除")

        # Create Save and Clear buttons for Model settings
        self.model_save_btn = QPushButton("保存")
        self.model_clear_btn = QPushButton("清除")

        # Connect button clicks to functions
        self.neo4j_btn.clicked.connect(self.show_neo4j_settings)
        self.model_btn.clicked.connect(self.show_model_settings)
        self.neo4j_save_btn.clicked.connect(self.on_neo4j_save_click)
        self.neo4j_clear_btn.clicked.connect(self.on_neo4j_clear_click)
        self.model_save_btn.clicked.connect(self.on_model_save_click)
        self.model_clear_btn.clicked.connect(self.on_model_clear_click)

        # Initialize 'graph' attribute as None initially
        self.graph = None
        self.neo4j_saved = False

        # Set up main layout
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout(self.main_widget)
        self.main_layout.addWidget(self.neo4j_btn)
        self.main_layout.addWidget(self.model_btn)
        self.main_layout.addWidget(self.input_label)
        self.main_layout.addWidget(self.input_textbox)
        self.main_layout.addWidget(self.output_label)
        self.main_layout.addWidget(self.output_textbox)

        self.setCentralWidget(self.main_widget)

        # Create and hide the Neo4j settings widget
        self.neo4j_settings_widget = QWidget()
        self.neo4j_layout = QVBoxLayout(self.neo4j_settings_widget)
        self.neo4j_layout.addWidget(self.neo4j_url_label)
        self.neo4j_layout.addWidget(self.neo4j_url_input)
        self.neo4j_layout.addWidget(self.neo4j_username_label)
        self.neo4j_layout.addWidget(self.neo4j_username_input)
        self.neo4j_layout.addWidget(self.neo4j_password_label)
        self.neo4j_layout.addWidget(self.neo4j_password_input)
        self.neo4j_layout.addWidget(self.neo4j_save_btn)
        self.neo4j_layout.addWidget(self.neo4j_clear_btn)
        self.neo4j_layout.addStretch(1)
        self.neo4j_settings_widget.hide()  # Hide the Neo4j settings widget

        # Create and hide the Model settings widget
        self.model_settings_widget = QWidget()
        self.model_layout = QVBoxLayout(self.model_settings_widget)
        self.model_layout.addWidget(self.api_label)
        self.model_layout.addWidget(self.api_input)
        self.model_layout.addWidget(self.model_save_btn)
        self.model_layout.addWidget(self.model_clear_btn)
        self.model_layout.addStretch(1)
        self.model_settings_widget.hide()  # Hide the Model settings widget

        # Create Save and Clear buttons for output text box
        self.output_save_btn = QPushButton("提交")
        self.output_clear_btn = QPushButton("清除")

        # Connect button clicks to functions
        self.output_save_btn.clicked.connect(self.on_input_output_save_click)
        self.output_clear_btn.clicked.connect(self.on_input_output_clear_click)

        # Add Save and Clear buttons for output text box
        self.main_layout.addWidget(self.output_save_btn)
        self.main_layout.addWidget(self.output_clear_btn)

        self.contact_us_btn = QPushButton("联系我们")
        self.contact_us_btn.clicked.connect(self.show_contact_us_dialog)
        self.main_layout.addWidget(self.contact_us_btn)

        self.setCentralWidget(self.main_widget)

        # 创建“关于”按钮
        self.about_btn = QPushButton("关于此系统")
        self.about_btn.clicked.connect(self.show_about_dialog)

        # 在设置主窗口的中央小部件之前，把“关于”按钮添加到布局中
        self.main_layout.addWidget(self.about_btn)

        # 将主窗口的中央小部件设置为 main_widget
        self.setCentralWidget(self.main_widget)

    def show_neo4j_settings(self):
        if not self.neo4j_settings_widget.isVisible():
            self.neo4j_settings_widget.setWindowTitle("Neo4j设置")  # 设置 Neo4j 设置子框的标题
            self.neo4j_settings_widget.show()
            self.neo4j_btn.setText("隐藏Neo4j设置")
        else:
            self.neo4j_settings_widget.hide()
            self.neo4j_btn.setText("Neo4j设置")

    def show_model_settings(self):
        if not self.model_settings_widget.isVisible():
            self.model_settings_widget.setWindowTitle("Model设置")  # 设置 Model 设置子框的标题
            self.model_settings_widget.show()
            self.model_btn.setText("隐藏Model设置")
        else:
            self.model_settings_widget.hide()
            self.model_btn.setText("Model设置")

    def on_neo4j_save_click(self):
        # Get the input from the "URL", "Username", and "Password" input boxes
        url = self.neo4j_url_input.text()
        username = self.neo4j_username_input.text()
        password = self.neo4j_password_input.text()

        if not url or not username or not password:
            QMessageBox.warning(self, "警告", "请填写完整Neo4j设置")
            return

        # Create a Neo4jGraph instance with the user-provided information
        self.graph = Neo4jGraph(url=url, username=username, password=password)
        self.neo4j_saved = True

        QMessageBox.information(self, "提示", "Neo4j保存按钮被点击了")

    def on_neo4j_clear_click(self):
        # Clear the content of "URL", "Username", and "Password" input boxes
        self.neo4j_url_input.clear()
        self.neo4j_username_input.clear()
        self.neo4j_password_input.clear()

        # Show QMessageBox with parent set to self (MyMainWindow)
        message_box = QMessageBox(self)
        message_box.setText("Neo4j内容被清除")
        message_box.setWindowTitle("提示")
        message_box.exec()

    def on_model_save_click(self):
        # Get the input from the "API" input box
        api_key = self.api_input.text()

        # Check if Neo4j settings have been saved
        if not self.neo4j_saved:
            QMessageBox.warning(self, "警告", "请先保存Neo4j设置")
            return

        # Create ChatOpenAI instance with temperature=0 and user-provided API key
        chat_model = ChatOpenAI(temperature=0, openai_api_key=api_key)

        # Make sure 'self.graph' is not None before creating the chain
        if self.graph is not None:
            # Create the GraphCypherQAChain instance using the ChatOpenAI model and the Neo4jGraph.
            self.chain = GraphCypherQAChain.from_llm(chat_model, graph=self.graph, verbose=True)
            QMessageBox.information(self, "提示", "Model已经被保存")
        else:
            QMessageBox.warning(self, "警告", "请先保存Neo4j设置")

        QMessageBox.information(self, "提示", "Model保存按钮被点击了")

    def on_model_clear_click(self):
        # Clear the content of "API" input box
        self.api_input.clear()

        message_box = QMessageBox(self)
        message_box.setText("model内容被清除")
        message_box.setWindowTitle("提示")
        message_box.exec()

    def on_input_output_save_click(self):
        # 获取输入框的内容
        input_text = self.input_textbox.toPlainText()

        # 确保 Neo4j 设置已保存
        if not self.neo4j_saved:
            QMessageBox.warning(self, "警告", "请先保存 Neo4j 设置")
            return

        # 确保模型已保存，并且输入框不为空
        if not hasattr(self, 'chain') or not input_text.strip():
            QMessageBox.warning(self, "警告", "请先保存模型或输入内容")
            return
        # 使用 ChatOpenAI 模型处理输入，得到输出
        output_text = self.chain.run(f"""{input_text}""")

        # 将输出显示在输出框中
        self.output_textbox.setPlainText(output_text)

        QMessageBox.information(self, "提示", "已提交，请稍等")

    def on_input_output_clear_click(self):
        # Clear the content of input_textbox and output_textbox
        self.input_textbox.clear()
        self.output_textbox.clear()

        QMessageBox.information(self, "提示", "输入和输出框已经被清除")

    def show_contact_us_dialog(self):
        # 创建一个 QDialog 作为对话框
        contact_us_dialog = QDialog(self)
        contact_us_dialog.setWindowTitle("联系我们")

        # 创建一个 QVBoxLayout 布局，并将其设置为对话框的布局
        layout = QVBoxLayout(contact_us_dialog)

        # 添加联系我们的文本，使用 HTML 标签设置字体样式
        contact_us_label = QLabel()
        contact_us_label.setStyleSheet("font-size: 18px; font-family: Arial; text-align: center;")
        contact_us_label.setText("作者：李福临<br>联系方式：15036721032")
        layout.addWidget(contact_us_label)

        # 创建一个 QLabel，并将包含图片的 QPixmap 设置为它的图像
        contact_us_image_label = QLabel()
        contact_us_image = QPixmap("contact_us_image.jpg")  # 替换为实际图片路径
        contact_us_image_label.setPixmap(contact_us_image)
        layout.addWidget(contact_us_image_label)

        # 将布局添加到对话框
        contact_us_dialog.setLayout(layout)

        # 显示对话框
        contact_us_dialog.exec()

    def show_about_dialog(self):
        # 创建一个 QDialog 用于“关于”对话框
        about_dialog = QDialog(self)
        about_dialog.setWindowTitle("关于本系统")

        # 创建一个 QVBoxLayout 并将其设置为对话框的布局
        layout = QVBoxLayout(about_dialog)

        # 添加介绍性文本，使用 QLabel 和 HTML 标签设置样式
        about_text = """
        <h2>欢迎使用史谈文博系统 v1.0</h2>
        <p>在本系统的“Neo4j”和“Model”设置中您均可以调整其为自己的数据以及模型。</p>
        <p>在两个设置模块的下方，本系统提供了一个交互界面，您可以向它提问，然后它会回答您的问题。</p>
        <p>请在左侧输入框中输入问题，然后点击提交按钮，在输出框查看回答。</p>
        <p>我们希望您在使用过程中有愉快的体验。</p>
        <p>如果您在使用过程中有任何问题，欢迎点击“联系我们”界面，扫码与作者进行沟通。</p>
        <h3>期待史谈文博系统 v2.0</h3>
        <p>在史谈文博系统 v2.0，我们希望在其中可以加入语音转文字输入功能以及长对话记忆功能。</p>
        <p>期待您的喜欢与支持，如果您有更好的想法，也欢迎与我们进行合作。</p>
        """
        about_label = QLabel()
        about_label.setStyleSheet("font-size: 16px; font-family: Arial;")
        about_label.setText(about_text)
        layout.addWidget(about_label)

        # 添加一张图片，使用 QLabel 和 QPixmap
        about_image_label = QLabel()
        about_image = QPixmap("about_us.jpg")  # 替换为实际的图片路径
        about_image_label.setPixmap(about_image)
        layout.addWidget(about_image_label)

        # 设置对话框的布局
        about_dialog.setLayout(layout)

        # 显示对话框
        about_dialog.exec()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())
