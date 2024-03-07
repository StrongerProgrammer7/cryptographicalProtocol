from MyMath import MyMath
import openpyxl

class TestFerma(MyMath):

    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.sheet = self.wb.active

    def testFeram(self,base,num):
        return pow(base,num-1,num)

    def testFerma100(self,num,singleNum=True):
        if singleNum:
            self.sheet.append(["Число"] + [f"{i} тест" for i in range(1, 100)])
        listResult = [num]
        for i in range(2,101):
            if self.testFeram(i,num) == 1:
               # print(f"Test {i} num:{num} is simple")
                listResult.append("+")
            else:
                #print(f"Test {i} num:{num} is composite")
                listResult.append("-")

        self.sheet.append(listResult)
        if singleNum:
            self.wb.save("fermat_test_results.xlsx")

    def getListCompositeNumbers(self):
        #для которых первое прохождение теста выдает ответ простое
        listCompositeButTestFermaSimple = []

        for i in range(2, 10000000):
            if MyMath.factorizeIntoTwoNumbers(i) is not None:
                #print(f"{i} is composite next check test ferma")
                if self.testFeram(2,i) == 1:
                    #print(f"First test ferma: {i} is Simple!")
                    listCompositeButTestFermaSimple.append(i)

        #print(listCompositeButTestFermaSimple)
        if len(listCompositeButTestFermaSimple) > 0:
            self.sheet.append(["Число"] + [f"{i} тест" for i in range(1, 100)])
            for elem in listCompositeButTestFermaSimple:
                self.testFerma100(elem,False)
            self.wb.save("fermat_test_results.xlsx")



