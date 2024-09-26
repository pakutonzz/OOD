def find_max_index(arr, start, max_idx=None):
    if start == -1:
        return max_idx
    if max_idx is None:
        max_idx = start
    if arr[start] > arr[max_idx]:
        max_idx = start
    return find_max_index(arr, start - 1, max_idx)

def straight_selection_sort(arr, end=None):
    if end is None:
        end = len(arr) - 1
    
    if end == 0:
        return

    max_idx = find_max_index(arr, end)

    if max_idx != end:
        print(f"swap {arr[end]} <-> {arr[max_idx]} : ", end="")
        arr[end], arr[max_idx] = arr[max_idx], arr[end]
        print(arr)

    straight_selection_sort(arr, end - 1)

input_arr = list(map(int, input("Enter Input : ").split()))

straight_selection_sort(input_arr)


print(input_arr)
