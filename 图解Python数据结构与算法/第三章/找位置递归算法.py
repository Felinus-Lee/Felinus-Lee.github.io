def find_seat_recursive(current_row):
    if current_row == 1:
        return 1  # 第一排的人是确定的，排数为1
    else:
        # 向前方询问，递归调用
        previous_row = find_seat_recursive(current_row - 1)
        print(f"前一排的人员说他们在第 {previous_row} 排")
        return previous_row + 1  # 在前一排的基础上加1，得到当前排数