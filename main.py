import random

def password():
    s1 = ['a','b','c','v','n','m','l','k','j','h','g','f','t']
    s2 = ['A','B','C','B','N','M','L','K','J','H','G','F','T']
    result = ''
    for i in range(11):
        result += random.choice(s1+s2)
    return result

p = password()
print(p)
