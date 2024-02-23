from CalculatorFieldGalua2.CalcFieldGalua2 import CalcFieldGalua2

class CalculatorPolynomGalua(CalcFieldGalua2):

    def __init__(self):
        super().__init__()

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
            print("8. Показать полиномы")
            print("9. Выход")

            choice = input("Введите номер действия (1-9): ")

            if choice == "9":
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
                elif choice == "8":
                    print(f"Irredicuble polynom : {self.irreduciblePolynom}")
                    print(f"Polynoms: 1. {self.polynom1}     2. {self.polynom2}")
            else:
                print("Ошибка: введите число от 1 до 9.")

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
            else:
                if polynom[ind] > 0:
                    strbin += "0" * (polynom[ind])

        print(strpoly + " (" + strbin + " )")
