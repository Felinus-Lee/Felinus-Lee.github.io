def find_seat(target_row):
    current_row = 0  # 初始排数为0

    while current_row != target_row:
        print(f"当前所在排数：{current_row}")
        current_row += 1  # 排数加1，走到下一排

    print(f"找到目标排数：{target_row}")