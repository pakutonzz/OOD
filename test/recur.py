def sort(arr, n=None):
    if n is None:
        n = len(arr)

    if n<2 :
        return arr
    
    

    last = arr[n-1]
    j = n-2

    def insert():
        nonlocal j
        if j >= 0 and arr[j] > last :
            arr[j+1] = arr[j]
            j -= 1
            insert()
        else:
            arr[j+1] = last
    
    insert()
    sort(arr, n-1)
    return arr

inp = input('Enter your List : ')
nums = list(map(int, inp.split(',')))
print(f'List after Sorted : {sort(nums)}')