from MyMath import MyMath
from helper import swap


class CalculatorPolynomGalua(MyMath):

    def __init__(self, irreduciblePolynom):

        self.irreduciblePolynom = irreduciblePolynom
        self.maxPower = max(irreduciblePolynom)

    def runCalculator(self):

        while (True):
            # TODO: input choose
            print("Input")
    def GCDPolynom(self,polynom1,polynom2):
        maxDegree1 = max(polynom1)
        maxDegree2 = max(polynom2)
        if maxDegree2 >  maxDegree1:
            polynom1,polynom2 = swap(polynom1,polynom2)
        while True:
            q,r = self.divmodPolynoms(polynom1,polynom2)
            polynom1 = polynom2
            polynom2 = r
            if len(polynom2) == 0:
                return polynom1
            elif len(polynom2) == 1:
                return [0]

    def upPolynomByDegree(self,polynom: list,degree: int):
        result = []
        for elem in polynom:
            result.append(elem*degree)
        if max(result) > self.maxPower:
            _,result = self.divmodPolynoms(result,self.irreduciblePolynom)
        return result

    def multmodPolynom(self, polynom1, polynom2):
        result = self._multPolynoms(polynom1, polynom2)
        _, r = self.divmodPolynoms(result, self.irreduciblePolynom)
        return r

    def _multPolynoms(self, polynom1, polynom2):
        result = []
        for elem1 in polynom1:
            for elem2 in polynom2:
                result = self.xorPolynoms(result, [elem1 + elem2])
        return result

    # FIX: Not work with small degree
    def multPolynomsInBite(self, poly1, poly2):
        maxDegreePoly1 = max(poly1)
        maxDegreePoly2 = max(poly2)
        if maxDegreePoly1 > maxDegreePoly2:
            poly1, poly2 = swap(poly1, poly2)
            maxDegreePoly1, maxDegreePoly2 = swap(maxDegreePoly1, maxDegreePoly2)

        binPoly1 = self._fromArrayBinToNum(self._fromDegreeToBinaryArray(poly1))
        binPoly2 = self._fromArrayBinToNum(self._fromDegreeToBinaryArray(poly2))

        irreduciblePolynom = self._fromDegreeToBinaryArray(self.irreduciblePolynom)
        irreduciblePolynom.pop(0)
        binIrreduciblePolynom = self._fromArrayBinToNum(irreduciblePolynom)

        maxBit = self.maxPower - 1
        result = []
        for i in range(0, maxDegreePoly1):
            seniorBit = MyMath.get_bit(binPoly2, maxBit)
            binPoly2 = MyMath.shit_bit(binPoly2, 1, self.maxPower)
            print(format(binPoly2, 'b'))
            if seniorBit == 1:
                binPoly2 = binPoly2 ^ binIrreduciblePolynom
            else:
                if MyMath.get_bit(binPoly2, maxBit) != 1:
                    result.append(binPoly2)
            print(format(binPoly2, 'b'))

        for i in result:
            binPoly1 = binPoly1 ^ i

        return binPoly1

    def divmodPolynoms(self, polynom1, polynom2):
        if polynom1[0] < polynom2[0]:
            return polynom1
        div = []
        r = []
        while True:
            elem = polynom1[0]
            factor = elem - polynom2[0]
            if factor > -1:
                polynom = self._multPolynoms([factor], polynom2)
                polynom = self.xorPolynoms(polynom1, polynom)
                r = polynom
                div.append(factor)
                polynom1 = polynom
            else:
                return div, r
            if len(polynom1) == 0:
                return div,r

        return div, r

    def xorPolynoms(self, polynom1, polynom2):
        if len(polynom1) == 0:
            return polynom2
        elif len(polynom2) == 0:
            return polynom1
        polynom1 = self._fromDegreeToBinaryArray(polynom1)
        polynom2 = self._fromDegreeToBinaryArray(polynom2)
        if len(polynom1) > len(polynom2):
            polynom2 = self._addZeroToBegin(polynom2, len(polynom1))
        else:
            polynom1 = self._addZeroToBegin(polynom1, len(polynom2))

        xor = self._xorPolynoms(polynom1, polynom2)
        return self._fromBinaryArrayToDegree(xor)

    def _xorPolynoms(self, polynom1, polynom2):
        result = []
        for i in range(len(polynom1)):
            result.append(polynom1[i] ^ polynom2[i])
        return result

    def _xorPolynomParallelMult(self, polynom, elem):
        if elem in polynom:
            index = polynom.index(elem)
            polynom.pop(index)
        else:
            polynom.append(elem)
        return polynom

    def _fromDegreeToBinaryArray(self, polynom):
        # 0 1 2 3 4
        # 8 4 3 1 0 = 100011010
        maxDegree = max(polynom)
        result = [0] * (maxDegree + 1)
        for deg in polynom:
            result[maxDegree - deg] = 1
        return result

    def _fromBinaryArrayToDegree(self, polynom):
        result = []
        for i in range(len(polynom)):  # len(polynom)-1,-1,-1):
            if polynom[i] != 0:
                result.append(len(polynom) - 1 - i)
        return result

    def _addZeroToBegin(self, polynom: list, max_length):
        for i in range(len(polynom), max_length):
            polynom.insert(0,0)
        return polynom

    def _fromArrayBinToNum(self, arr):
        degree = len(arr) - 1
        result = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                result += pow(2, degree)
            degree -= 1
        return result
