class Calculator :
    def __init__(self,num) -> None:
        self.__num = num
    
    def __add__(self, other):
        return self.__num + other.__num
    def __sub__(self, other):
        return self.__num - other.__num
    def __mul__(self, other):
        return self.__num * other.__num
    def __truediv__(self, other):
        return self.__num / other.__num

x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))

print(x+y,x-y,x*y,x/y,sep = "\n")