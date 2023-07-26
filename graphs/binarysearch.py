def binary_search(list, target):
    l = 0
    r = len(list)-1
    while l <= r:
        m = l + (r-l)/2

        if list[m] == target:
            return m
        
        if list[m] > target:
            r = m-1
        else:
            l = m+1
    return -1