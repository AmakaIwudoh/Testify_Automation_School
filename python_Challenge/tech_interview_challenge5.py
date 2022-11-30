# 5. Rite  a  Python  program  that  checks  if  a  string  is  apalindrome,
# Then  optionally  write  a  unit  test  to  check your program's correctness.

def is_a_palindrome(string):
    if string == string[::-1]:
        print(string, "Is Palindrome")

is_a_palindrome("civic")
is_a_palindrome("level")
is_a_palindrome("number")
is_a_palindrome("Madam")
is_a_palindrome("age")