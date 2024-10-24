#快速排序框架
def quick_sort(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        quick_sort(data, left, mid - 1)
        quick_sort(data, mid + 1, right)

#partition部分
def partition(li, left, right):
    tmp = li[left]  # 选择基准元素，这里简单地选择数组的第一个元素作为基准元素
    while left < right:
        # 从右向左找到第一个小于基准元素的元素
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]  # 将找到的小于基准元素的元素移到左边

        # 从左向右找到第一个大于基准元素的元素
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]  # 将找到的大于基准元素的元素移到右边
        print(li)
    li[left] = tmp  # 将基准元素放置到最终的位置
    return left  # 返回基准元素最终的位置，这个位置将用于将数组分为两部分