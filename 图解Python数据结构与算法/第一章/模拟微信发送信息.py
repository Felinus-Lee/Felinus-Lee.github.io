from queue import Queue

class WeChatUser:
    def __init__(self, name):
        self.name = name
        self.message_queue = Queue()

    def send_message(self, message, recipient):
        print(f"{self.name}发送消息给{recipient.name}：{message}")
        recipient.receive_message(message)

    def receive_message(self, message):
        print(f"{self.name}收到消息：{message}")
        self.message_queue.put(message)
        print(f"{self.name}的消息队列内容：{list(self.message_queue.queue)}")

def main():
    # 创建两个用户
    xiaomei = WeChatUser("小美")
    xiaoshuai = WeChatUser("小帅")

    # 小帅发送消息给小美
    xiaoshuai.send_message("你好，小美！", xiaomei)

    # 模拟消息队列
    while not xiaomei.message_queue.empty():
        message = xiaomei.message_queue.get()
        print(f"{xiaomei.name}收到消息：{message}")

    # 显示最终消息队列状态
    print(f"{xiaomei.name}的最终消息队列内容：{list(xiaomei.message_queue.queue)}")

if __name__ == "__main__":
    main()
