def gcdBruteForce(num1, num2):
    min_num = min(num1, num2)
    max_num = max(num1, num2)

    curr = min_num

    while (curr > 1):
        if (max_num % curr == 0) and (min_num % curr == 0):
            return curr
        
        curr -= 1

    return curr

def gcdEuclideanAlgorithm(num1, num2):
    min_num = min(num1, num2)
    max_num = max(num1, num2)

    remainder = max_num % min_num

    gcd = 0

    if (remainder != 0):
        gcd = gcdEuclideanAlgorithm(min_num, remainder)
    else:
        gcd = min_num

    return gcd

# x = gcdBruteForce(3, 5)
# x = gcdBruteForce(3, 7)
# x = gcdBruteForce(3, 21)
# x = gcdBruteForce(15, 70)
# print(x)

x = gcdEuclideanAlgorithm(3, 5)
x = gcdEuclideanAlgorithm(3, 7)
x = gcdEuclideanAlgorithm(3, 21)
x = gcdEuclideanAlgorithm(15, 70)
print(x)

