w = input("Enter Input : ")

result = abs(w.count("(") - w.count(")")) + abs(w.count("[") - w.count("]"))
print(result)

if result == 0 :
    print("Perfect ! ! !")