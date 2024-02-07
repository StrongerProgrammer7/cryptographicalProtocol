from math import gcd, sqrt,floor
from helper import is_prime,valueFunctionEuler

def comparisonsOfTheFirstDegree(a, b, mod):
    NOD = gcd(a, mod)
    print(NOD)
    # x=b*a^(f(n)-1) mod m


if __name__ == '__main__':
    print(f"Run {5 % 2}")
    comparisonsOfTheFirstDegree(5, 14, 7)

