def divisors(integer):
    from math import sqrt
    rst = []
    for i in range(2, int(sqrt(integer))):
        if integer % i == 0:
            rst.append(i)