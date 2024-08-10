def sift(li, low, high):
    i = low  # i最开始指向根节点
    j = 2 * i + 1  # j开始是左孩子
    tmp = li[low]  # 把堆顶存起来
    while j <= high:  # 只要j和j+1位置有节点
        if j + 1 <= high and li[j + 1] > li[j]:
            j = j + 1  # j指向右孩子
        if li[j] > tmp:
            li[i] = li[j]
            i = j  # 往下看一层
            j = 2 * i + 1
        else:  # tmp更大,把tmp放在i的位置上
            li[i] = tmp  # 把tmp放在某一级领导位置上
            break
    else:
        li[i] = tmp  # 把tmp放在叶子节点上

def heap_sort(li):
    n = len(li)
    for i in range((n - 2) // 2, -1, -1):
        sift(li, i, n - 1)
    # 建堆完成了
    for i in range(n - 1, -1, -1):
        # i指向当前堆的最后一个节点
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)  # i-1是新的high
