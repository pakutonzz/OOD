def insertion_sort(arr, n=None) :
    if n is None:
        n = len(arr)

    if n<2 :
        return arr
    
    insertion_sort(arr,n-1)

    last = arr[n-1]
    j = n-2

    def insert():
        nonlocal j
        if j >= 0 and arr[j] < last :
            arr[j+1] = arr[j]
            j -= 1
            insert()
        else:
            arr[j+1] = last
    
    insert()
    return arr

inp = input('Enter your List : ')
nums = list(map(int, inp.split(',')))
print(f'List after Sorted : {insertion_sort(nums)}')