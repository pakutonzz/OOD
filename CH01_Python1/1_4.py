def odd_list(al):
    opls = []
    for i in al:
        if i%2 == 1:
            opls.append(i)
    return opls

print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)