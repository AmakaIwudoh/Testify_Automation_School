# 4 Writing  a  well-documented  code  creates  a  function
# that calculates simple interest

def simpleIntrest(P, R, T):
    I = P * R * T
    return I


get_simpleInterest = simpleIntrest(10, 0.5, 4)
print(get_simpleInterest)