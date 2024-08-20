def Factorial(n) :
    n = int(n)
    if n > 1 :
        return n * Factorial(n-1)
    return 1

n = input('Enter Number : ')
print(f'{n}! = {Factorial(n)}')