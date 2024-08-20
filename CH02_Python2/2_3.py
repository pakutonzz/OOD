def mod_position(arr, s):
    s = int(s)
    output = []
    for i in range(1, len(arr) + 1):
        if i % s == 0:
            output.append(arr[i-1])
    return output

print("*** Mod Position ***")
arr, s = input("Enter Input : ").split(',')
print(mod_position(arr,s))