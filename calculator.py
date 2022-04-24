class Calculator:
    def __init__(self, num1=0, num2=0, sign="+"):
        self.__num1 = num1
        self.__num2 = num2
        self.__sign = sign
        self.answer = self.__calculate()

    def __call__(self, *args, **kwds):
        return self.answer

    def __calculate(self):
        r = eval(f"{self.__num1}{self.__sign}{self.__num2}")  # 5+9
        return r

    def __add__(self, other):
        try:
            return self.answer + other.answer
        except:
            return self.answer + other.answer

    def __sub__(self, other):
        try:
            return self.answer - other.answer
        except:
            return self.answer - other.answer

    def __mul__(self, other):
        try:
            return self.answer * other.answer
        except:
            return self.answer * other.answer

    def __truediv__(self, other):
        try:
            return self.answer / other.answer
        except:
            return self.answer / other.answer

    def __mod__(self, other):
        try:
            return self.answer % other.answer
        except:
            return self.answer % other.answer

    def __floordiv__(self, other):
        try:
            return self.answer // other.answer
        except:
            return self.answer // other


a = Calculator(6, 3, "/")
a1 = Calculator(63, 3, "/")

print(a - a1)

a += a1
print(a)

a *= 0
print(a)

a = a1 // 6
print(a)