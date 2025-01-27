def multiple_of_c(a,b,c):
    if a > b and b % c == 0:
        return (a // c) - (b // c -1)
    elif a > b and b % c != 0:
        return (a // c) - (b // c)
    elif a < b and a % c == 0:
        return (b // c) - (a // c -1)
    elif a < b and a % c != 0:
        return (b // c) - (a // c)

print(multiple_of_c(12,18,3))