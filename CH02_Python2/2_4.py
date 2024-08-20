def zero_sum(ar):
    arr = list(map(int, ar.split()))
    if len(arr)<3:
        return "Array Input Length Must More Than 2"

    size = len(arr)
    output = []

    for i in range(size - 2):
        for j in range(i + 1,size - 1):
            for k in range(j + 1,size):
                if arr[i] + arr[j] + arr[k] == 0 :
                    temp = [arr[i], arr[j], arr[k]]
                    if temp not in output :
                        output.append(temp)
    return output

ar = input('Enter Your List : ')
print(zero_sum(ar))


