from CalculatorFieldGalua2.CalcFieldGalua2 import CalcFieldGalua2

class CalculatorPolynomGalua(CalcFieldGalua2):

    def __init__(self):
        super().__init__()

    def _interactiveInput(self,message="Input degree x for polynom , through space\n Example: x^3+x+1 => 3 1 0\n",singleElem=False):
        while True:
            str = input(message)
            entry = self._checkInput(str)
            if entry is not None:
                if singleElem == True:
                    return entry[0]
                return entry

    def _checkInput(self, str):
        if all(char.isdigit() or char.isspace() for char in str):
            arrayNumb = [int(num) for num in str.split() if int(num) >= 0 ]
            print("Your input:")
            arrayNumb.sort(reverse=True)
            self.outputPolynom(arrayNumb)
            return arrayNumb
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
            print("8. Показать полиномы")
            print("9. НОД")
            print("10. Выход")

            choice = input("Введите номер действия (1-10): ")

            if choice == "10":
                print("Выход из калькулятора.")
                break

            if choice in ["1", "2", "3", "4","5","6","7","8","9"]:
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
                    degree = self._interactiveInput("Input degree (is N)",singleElem=True)
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
                    self.outputTableMul(result)
                elif choice == "6":
                    print("Input polynom1: ")
                    self.polynom1 = self._interactiveInput()
                    print("Input polynom2")
                    self.polynom2 = self._interactiveInput()
                elif choice == "7":
                    print("Input irreducible polynom")
                    self.irreduciblePolynom = self._interactiveInput()
                    self.maxPower = max(self.irreduciblePolynom)
                elif choice == "8":
                    print(f"Irredicuble polynom : {self.irreduciblePolynom}")
                    print(f"Polynoms: 1. {self.polynom1}     2. {self.polynom2}")
                elif choice == "9":
                    result = self.GCDPolynom(self.polynom1,self.polynom2)
                    print(f"НОД{result}")
            else:
                print("Ошибка: введите число от 1 до 9.")

    def outputPolynom(self, polynom):
        strbin = ""
        strpoly = ""
        for ind in range(len(polynom)):
            strbin += "1"
            strpoly += f"x^{polynom[ind]}+"
            if ind < len(polynom) - 1:
                diff = polynom[ind] - polynom[ind + 1]
                if diff > 1:
                    strbin += "0" * (diff - 1)
            else:
                if polynom[ind] > 0:
                    strbin += "0" * (polynom[ind])

        print(strpoly + " (" + strbin + " )")

    def outputTableMul(self,table):
        str = ""
        max_bit = []
        for i in range(1,pow(2,self.maxPower)):
            str += format(i, f'0{self.maxPower}b') + ' | '
            if i == pow(2,self.maxPower) - 1:
                max_bit.append(format(i, f'0{self.maxPower}b'))
        #str.reverse()
        print(str)
        str = ''
        ind = 0
        for i in range(pow(2,self.maxPower)-1):
            str += format(i+1, f'0{self.maxPower}b') + f' - {max_bit[0]} | '
            for j in range(i,pow(2,self.maxPower)-1):
                if j >= i and ind < len(table):
                    str += f'{(table[ind])} | '
                    ind+=1
            str +='\n'
        print(str)
