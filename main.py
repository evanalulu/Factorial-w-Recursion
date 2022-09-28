def fact(n):
    # Base Case:
    if (n == 1 or n == 0):
        return 1

    # Recursive Case:
    return (fact(n-1)*n)

print(fact(4))