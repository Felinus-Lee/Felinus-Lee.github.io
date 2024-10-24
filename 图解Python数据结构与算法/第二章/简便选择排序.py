def select_sort_simple(li):
    li_new=[]
    for i in range(len(li)):
        min_val=min(li)
        li_new.append(min_val)
        li.remove(min_val)
        print(li_new)
    return li_new