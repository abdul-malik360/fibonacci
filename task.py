def fact(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * fact(x-1)
x = int(input("please enter number: "))
print(fact(x))


