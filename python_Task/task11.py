print("Function that accepts 2 numbers\n")


def add(num1=10, num2=15):
    result = num1 + num2
    print("Result:", result)


add(1, 2)
add()


print("\nFunction that returns String value\n")


def string(name):
    return name


str = string("Testify Python")
print(str)
