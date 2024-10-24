def kmp_search(text, pattern):
    def build_next_array(pattern):
        next_array = [-1] * len(pattern)
        j, k = 0, -1

        while j < len(pattern) - 1:
            if k == -1 or pattern[j] == pattern[k]:
                j += 1
                k += 1
                next_array[j] = k
            else:
                k = next_array[k]

        return next_array

    next_array = build_next_array(pattern)
    i, j = 0, 0

    while i < len(text) and j < len(pattern):
        if j == -1 or text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            j = next_array[j]

    if j == len(pattern):
        return i - j  # 返回匹配的起始位置
    else:
        return -1  # 未找到匹配