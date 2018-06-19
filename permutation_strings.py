"""Permutation Strings

What is the length of the shortest string on an alphabet of n symbols that
contains all n! permutations of the alphabet as (contiguous) substrings?

Please see "Permutation Strings" by Jeffrey A. Barnett for more information:
http://www.notatt.com/permutations.pdf
"""

import itertools

def permute(symbols):
    return [''.join(i) for i in itertools.permutations(symbols)]

def factorial(n):
    factorial = 1
    for i in range(2, n+1):
        factorial *= i
    return factorial

def expected(symbols):
    expected = 0
    for i in range(len(symbols)):
        expected += factorial(i+1)
    return expected

def coverage(permutations, string):
    coverage = 0
    for i in range(len(permutations)):
        if permutations[i] in string:
            coverage += 1
    return coverage

def complete(permutations, string):
    return coverage(permutations, string) == len(permutations)

def optimal(string, symbols):
    return expected(symbols) == len(string)

def verify(permutations, string, symbols):
    return complete(permutations, string) and optimal(string, symbols)

def shuffle(perm, attempt):
    i = (attempt // len(perm)) % len(perm)
    j = attempt % len(perm)
    perm[i], perm[j] = perm[j], perm[i]
    return perm

def shortest(symbols):
    if len(symbols) > 0:
        permutations = permute(symbols)
        perm = permute(symbols[:-1])
        SYM_LEN = len(perm[0])-1
        string = perm[0] + symbols[-1] + perm[0]
        perm.remove(perm[0])
        attempt = 0
        STRING = string
        PERM = perm
        verified = verify(permutations, string, symbols)
        while not verified:
            perm_len = len(perm)
            for i, j in itertools.product(range(SYM_LEN, 0, -1), range(perm_len)):
                if string[-i:] == perm[j][:i]:
                    string = string[:-i] + perm[j] + symbols[-1] + perm[j]
                    perm.remove(perm[j])
                    break
            if attempt > perm_len*perm_len:
                verified = True
            elif len(perm) == 0:
                verified = verify(permutations, string, symbols)
            if not verified and len(perm) == perm_len:
                attempt += 1
                string = STRING
                perm = shuffle(PERM, attempt)
        return string
    else:
        return ""

def calculate(symbols = ""):
    permutations = permute(symbols)
    string = shortest(symbols)
    print(string)
    print(coverage(permutations, string), len(permutations))
    print(len(string), expected(symbols))
    if not complete(permutations, string):
        print("FAIL")
    elif not optimal(string, symbols):
        print("WARNING")
    else:
        print("PASS")

if __name__ == '__main__':
    calculate(input())
