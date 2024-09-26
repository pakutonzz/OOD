def insert(arr, n):
    if n <= 1:
        return

    insert(arr, n - 1)

    last = arr[n - 1]
    j = n - 2

    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1
    
    arr[j + 1] = last

    if n == len(arr):
        print(f"insert {last} at index {j + 1} : {arr[:n]}")
    else:
        print(f"insert {last} at index {j + 1} : {arr[:n]} {arr[n:]}")

def recursive_insertion_sort(arr, n=None):
    if n is None:
        n = len(arr)
    
    insert(arr, n)
    
    if n == len(arr):
        print("sorted")
        print(arr)

input_arr = list(map(int, input("Enter Input : ").split()))

recursive_insertion_sort(input_arr)