def bubble_sort(li):
    for i in range(len(li)-1):  #i表示第i趟
        exchange=False
        for j in range(len(li)-i-1):  #箭头
            if li[j]<li[j+1]:  #此处为降序，改为大于号则变为升序
                li[j],li[j+1]=li[j+1],li[j]
                exchange=True
        if not exchange:
            return