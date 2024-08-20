def staircase(n, i=1):
    if n < 0 and  i <= abs(n) :
        print('_' *abs(i-1) + '#' * (abs(n)-i+1))
        return staircase(n, i+1)
    
    elif n > 0 and i <= n :
        print('_' *(n-i) + '#' * i)
        return staircase(n, i+1)
    
    elif n == 0 :
        return 'Not Draw!'
    return ''
    
print(staircase(int(input("Enter Input : "))))