# 8. Create a program that prints out the even numbers in an array.
# Sample array: a. [1, 2, 3, 4, 5, 6] b. [ 34, 2, 9, 91, 19,401, 0 ]


list1 = [1, 2, 3, 4, 5, 6]
for i in (list1):
  if i % 2 != 0:
    pass
  else:
    print(i,end=" ")


list2 = [34, 2, 9, 91, 19, 401, 0]
for j in (list2):
  if j % 2 != 0:
    pass
  else:
    print("\n", j,end=" ")