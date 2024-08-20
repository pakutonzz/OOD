def power(n, p):
    if p < 1 :
        return 1
    return n * power(n, p-1)

inp = input('Enter Input a b : ')
num,pow = map(int, inp.split())
print(power(num,pow))