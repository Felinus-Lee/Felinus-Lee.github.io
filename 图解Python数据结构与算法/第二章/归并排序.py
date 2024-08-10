# 定义一个合并函数，用于将两个已排序的子数组合并为一个有序数组  
def merge(li, low, mid, high):  
    # 初始化两个指针i和j，分别指向子数组的起始位置  
    i = low  
    j = mid + 1  
    # 创建一个临时列表ltmp，用于存储合并后的有序数组  
    ltmp = []  
      
    # 当两个子数组都有元素时，进行元素比较和添加到ltmp中  
    while i <= mid and j <= high:  
        if li[i] < li[j]:  
            ltmp.append(li[i])  
            i += 1  
        else:  
            ltmp.append(li[j])  
            j += 1  
      
    # 当一个子数组遍历完后，将另一个子数组的剩余元素添加到ltmp中  
    while i <= mid:  
        ltmp.append(li[i])  
        i += 1  
    while j <= high:  
        ltmp.append(li[j])  
        j += 1  
      
    # 将ltmp列表赋值给原数组li的对应切片，完成合并操作  
    li[low:high + 1] = list(ltmp)  # 这里需要转换ltmp为列表，以便赋值给原数组的切片  
  
# 定义一个归并排序函数，用于对整个数组进行排序  
def merge_sort(li, low, high):  
    # 如果数组长度小于2，则直接返回，因为一个元素或没有元素的数组默认是有序的  
    if low < high:  # 至少有两个元素，递归  
        # 找到中间索引  
        mid = (low + high) // 2  
        # 对左半部分子数组进行归并排序  
        merge_sort(li, low, mid)  
        # 对右半部分子数组进行归并排序  
        merge_sort(li, mid + 1, high)  
        # 合并左右两个已排序的子数组  
        merge(li, low, mid, high)