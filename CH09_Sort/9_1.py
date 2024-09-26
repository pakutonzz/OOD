def bubble_sort(arr):
    n = len(arr)
    step = 1
    sorted_flag = False

    for i in range(n - 1):
        swapped = False
        move_value = None

        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                move_value = arr[j + 1]

        if swapped:
            if i == n - 2:
                print(f"last step : {arr} move[{move_value}]")
            else:
                print(f"{step} step : {arr} move[{move_value}]")
            step += 1
        else:
            print(f"last step : {arr} move[None]")
            sorted_flag = True
            break

    if not sorted_flag and step == 1:
        print(f"last step : {arr} move[None]")

input_arr = list(map(int, input("Enter Input : ").split()))
bubble_sort(input_arr)
