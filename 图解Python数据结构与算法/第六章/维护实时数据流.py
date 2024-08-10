import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = []  # 最大堆，用于存储较小的一半数据
        self.min_heap = []  # 最小堆，用于存储较大的一半数据

    def add_num(self, num):
        # 插入到最大堆
        heapq.heappush(self.max_heap, -num)
        
        # 保证最大堆的最大值不大于最小堆的最小值
        if self.max_heap and self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        # 平衡堆的大小
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0

# 示例数据流
data_stream = [10, 20, 15, 30, 40, 5, 25]

median_finder = MedianFinder()
for num in data_stream:
    median_finder.add_num(num)
    print(f"Current median after adding {num}: {median_finder.find_median()}")
