def mindif_recursive(inp, index=0, sour=1, bitter=0, used=False):
    if index == len(inp):
        if not used:  # If no ingredient has been used, skip this combination
            return float('inf')
        return abs(sour - bitter)

    # Include the current ingredient
    include_diff = mindif_recursive(inp, index + 1, sour * inp[index][0], bitter + inp[index][1], True)

    # Exclude the current ingredient
    exclude_diff = mindif_recursive(inp, index + 1, sour, bitter, used)

    return min(include_diff, exclude_diff)

inps = input("Enter Input : ")
inp = [tuple(map(int, item.split())) for item in inps.split(',')]
result = mindif_recursive(inp)
print(result)
