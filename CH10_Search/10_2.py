def searching(target, arr):
    for i in range(len(arr)):
        if arr[i] > target:
            return arr[i]
    return "No First Greater Value"


inp, targets = input("Enter Input : ").split("/")
inp = list(map(int, inp.split()))
targets = list(map(int, targets.split()))

inp = sorted(inp)

for target in targets:
    print(searching(target, inp))