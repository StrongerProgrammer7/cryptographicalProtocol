from MyMath import MyMath
from helper import swap


class CalculatorPolynomGalua(MyMath):

    def __init__(self):
        print("Welcome to interactive calculator Polynom GF(2^m)")
        self.irreduciblePolynom = self._interactiveInput()
        #self.irreduciblePolynom = irreduciblePolynom
        self.maxPower = max(self.irreduciblePolynom)

    def _interactiveInput(self,message="Input degree x for polynom , through space\n Example: x^3+x+1 => 3 1 0\n"):
        while True:
            str = input(message)
            poly = self._checkInput(str)
            if poly is not None:
                return poly

    def _checkInput(self, str):
        if all(char.isdigit() or char.isspace() for char in str):
            poly = [int(num) for num in str.split() if int(num) >= 0 ]
            print("Your input:")
            poly.sort(reverse=True)
            self._outputPolynom(poly)
            return poly
        else:
            print("Not correct word === > " + str + " Using N digit and space")
            return None


    def runCalculator(self):
        print("Input polynom1: ")
        self.polynom1 = self._interactiveInput()
        print("Input polynom2")
        self.polynom2 = self._interactiveInput()

        while (True):
            print("Выберите действие:")
            print("1. Сложение")
            print("2. Умножение")
            print("3. Деление(целое остаток)")
            print("4. Возведение в степень")
            print("5. Построить таблицу умножения")
            print("6. Сменить полиномы")
            print("7. Сменить неприводимый полином")
            print("8. Выход")

            choice = input("Введите номер действия (1-8): ")

            if choice == "8":
                print("Выход из калькулятора.")
                break

            if choice in ["1", "2", "3", "4","5","6","7"]:
                if choice == "1":
                    result = self.xorPolynoms(self.polynom1,self.polynom2)
                    print(f"Результат сложения: {result}")
                elif choice == "2":
                    result = self.multmodPolynom(self.polynom1,self.polynom2)
                    print(f"Результат умножение: {result}")
                elif choice == "3":
                    result = self.divmodPolynoms(self.polynom1,self.polynom2)
                    print(f"Результат Деление: {result}")
                elif choice == "4":
                    degree = self._interactiveInput("Input degree (is N)")
                    print("Choose polynom:")
                    choice = input(f"1. {self.polynom1} , 2. {self.polynom2}")
                    if choice in ["1","2"]:
                        if choice == "1":
                            result = self.upPolynomByDegree(self.polynom1,degree[0])
                        elif choice == "2":
                            result= self.upPolynomByDegree(self.polynom2,degree[0])
                        print(f"Результат возведение в степень: {result}")
                    else:
                        print("Cancel")
                elif choice == "5":
                    result = self.createTableMultGalua()
                    print(result)
                elif choice == "6":
                    print("Input polynom1: ")
                    self.polynom1 = self._interactiveInput()
                    print("Input polynom2")
                    self.polynom2 = self._interactiveInput()
                elif choice == "7":
                    print("Input irreducible polynom")
                    self.irreduciblePolynom = self._interactiveInput()
            else:
                print("Ошибка: введите число от 1 до 8.")

    def GCDPolynom(self, polynom1, polynom2):
        maxDegree1 = max(polynom1)
        maxDegree2 = max(polynom2)
        if maxDegree2 > maxDegree1:
            polynom1, polynom2 = swap(polynom1, polynom2)
        while True:
            q, r = self.divmodPolynoms(polynom1, polynom2)
            polynom1 = polynom2
            polynom2 = r
            if len(polynom2) == 0:
                return polynom1
            elif len(polynom2) == 1:
                return [0]

    def createTableMultGalua(self):
        print(f" GF(2^{self.maxPower})")
        print("Created table")
        binaryNumbers: list[list] = []
        for i in range(pow(2, self.maxPower)):
            binary_representation = format(i, f'0{self.maxPower}b')  # Представляем число в двоичной системе
            truth_values = [int(bit) for bit in binary_representation]  # Преобразуем биты в целые числа
            binaryNumbers.append(truth_values)
        table: list[list] = []
        numbers = []
        for elem in binaryNumbers:
            numbers.append(self._fromBinaryArrayToDegree(elem))

        for i in range(1, len(numbers)):
            for j in range(i, len(numbers)):
                result = self.multmodPolynom(numbers[i], numbers[j])
                table.append(result)
                print(f"{result}")

        return table

    def upPolynomByDegree(self, polynom: list, degree: int):
        result = []
        for elem in polynom:
            result.append(elem * degree)
        if max(result) > self.maxPower:
            _, result = self.divmodPolynoms(result, self.irreduciblePolynom)
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
            return [], polynom1
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
            polynom.insert(0, 0)
        return polynom

    def _fromArrayBinToNum(self, arr):
        degree = len(arr) - 1
        result = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                result += pow(2, degree)
            degree -= 1
        return result

    def _outputPolynom(self, polynom):
        strbin = ""
        strpoly = ""
        for ind in range(len(polynom)):
            strbin += "1"
            strpoly += f"x^{polynom[ind]}+"
            if ind < len(polynom) - 1:
                diff = polynom[ind] - polynom[ind + 1]
                if diff > 1:
                    strbin += "0" * (diff - 1)

        print(strpoly + " (" + strbin + " )")
