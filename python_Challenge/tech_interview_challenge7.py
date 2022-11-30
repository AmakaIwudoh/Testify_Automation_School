# 7. Create a program that prints out the odd numbers in anarray.
# Sample array: a. [1, 2, 3, 4, 5, 6] b. [ 34, 2, 9, 91, 19,401, 0 ]

def printOddNumbers(arr):
    j = []
    for i in arr:
        if i % 2 != 0:
            j.append(i)
    print(j)


arr = [1, 2, 3, 4, 5, 6]
arrr = [34, 2, 9, 91, 19, 401, 0]
printOddNumbers(arr)
printOddNumbers(arrr)