
from Cryptodome.Random import get_random_bytes

from Cryptodome.Cipher import DES

class CryptoSystems:

    def __init__(self, MODE="DES.CBC"):
        if MODE == "DES.CBC":
            self.MODE = DES.MODE_CBC
        elif MODE == "DES.CFB":
            self.MODE = DES.MODE_CFB

    def generateKey(self,length):
        return get_random_bytes(length)

    def getANDArray(self,i, j):
        return [ia & ja for ia, ja in zip(i, j)]

    def getNotArray(self,i):
        return [not x for x in i]

    def getResultXorElemsOfArrays(self,i, j):
        return [ia ^ ja for ia, ja in zip(i, j)]

    # get the majority of results, i.e., if 2 or more of three values are the same
    def getTheElementThatOccursMostFrequently(self,i, j, k):
        return max([i, j, ], key=[i, j, k].count)

    def cyclicShiftRight(self, x: list, n: int):
        return x[-n:] + x[:-n]

    def shiftRight(self,x: list, n: int):
        return n * [0] + x[:-n] #включает в себя все элементы списка до

    # full binary adder
    def getListOfBits(self,i, j):
        # takes to lists of binaries and adds them
        length = len(i)
        listOfBits = list(range(length))
        # initial input needs an carry over bit as 0
        c = 0
        for x in range(length - 1, -1, -1):
            listOfBits[x] = i[x] ^ (j[x] ^ c)
            # carry over bit is equal the most represented, e.g., output = 0,1,0
            # then 0 is the carry over bit
            c = self.getTheElementThatOccursMostFrequently(i[x], j[x], c)

        return listOfBits

    def getXORZipArrays(self,listArrays):
        temp = []
        ind = 0
        while (ind < len(listArrays)):
            a = listArrays[ind]
            if ind < 1:
                b = listArrays[ind + 1]
                ind += 1
            else:
                b = temp
            result = self.getResultXorElemsOfArrays(a, b)
            temp = result
            ind += 1

        return temp
