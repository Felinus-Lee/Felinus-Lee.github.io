import heapq
import random

li = [3, 6, 5, 1, 8]
random.shuffle(li)

heapq.heapify(li)

result = []  # 用于记录弹出的元素和新数组的变化

n = len(li)
for i in range(n):
    popped_element = heapq.heappop(li)
    result.append(popped_element)  # 记录弹出的元素和新数组的变化
    print(f"弹出元素: {popped_element},旧数组:{li},新数组：{result}")
