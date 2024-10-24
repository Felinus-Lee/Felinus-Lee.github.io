import random

def guess_number_game():
    # 出题者提前想一个1到100之间的数字
    target = random.randint(1, 100)
    low, high = 1, 100  # 猜测范围

    print("我已经想好了一个1到100之间的数字，你能猜到它吗？")

    while True:
        # 猜测者选择中间位置的数字
        guess = (low + high) // 2
        print(f"你猜的数字是: {guess}")

        # 根据猜测结果，调整猜测范围
        if guess == target:
            print("恭喜！你猜对了。")
            break
        elif guess > target:
            print("猜大了。")
            high = guess - 1  # 缩小到左半部分
        else:
            print("猜小了。")
            low = guess + 1  # 缩小到右半部分

# 运行游戏
guess_number_game()
