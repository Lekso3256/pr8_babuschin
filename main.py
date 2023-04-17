import random

def password():
    s1 = ['a','b','c','v','n','m','l','k','j','h','g','f','t']

    result = ''
    for i in range(11):
        result += random.choice(s1)
    return result

p = password()
print(p)
