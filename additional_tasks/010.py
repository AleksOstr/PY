# Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :
#  "(p1**n1)(p2**n2)...(pk**nk)"
# with the p(i) in increasing order and n(i) empty if n(i) is 1.
# Example: n = 86240 should return "(2**5)(5)(7**2)(11)"


def prime_factors(n):
    a = []
    i = 2
    while i**2 <= n:
        if n % i == 0:
            a.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        a.append(n)
    result = ''
    for i in a:
        if a.count(i) == 1:
            result += f'({i})'
        else:
            if not f'({i}**{a.count(i)})' in result:
                result += f'({i}**{a.count(i)})'
    return result
    

print(prime_factors(777546000))






