# 6.  Write  a  function  that  removes  repeated  characters from a string.
# Sample Strings are:
# a. Hello: output should be Helo
# b. Concatenate: output should be Conaten

def remove_repeated_characters(strr):
    sta = ""
    for i in strr:
        if (i not in sta.casefold()):
            sta += i
    print(sta)


remove_repeated_characters('Hello')
remove_repeated_characters('Concatenate')