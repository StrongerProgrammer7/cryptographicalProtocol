import math

from ComparisonsOfTheFirstDegree import ComparisonsOfTheFirstDegree
from QuadraticResidues import QuadraticResidues
from CalculatorFieldGalua2.CalcFieldGalua2 import CalcFieldGalua2
from CalculatorFieldGalua2.CalculatorFieldGalua2 import CalculatorPolynomGalua


def outputSolutionComprasionOfTheFirstDegree():
    comparsion = ComparisonsOfTheFirstDegree()
    print(comparsion.comparisonsOfTheFirstDegree(5, 14, 7))
    print(comparsion.comparisonsOfTheFirstDegree(10, 13, 12))
    print(comparsion.comparisonsOfTheFirstDegree(18, 36, 35))
    print(comparsion.comparisonsOfTheFirstDegree(3, 19, 34))
    print(comparsion.comparisonsOfTheFirstDegree(5, 8, 21))
    print(comparsion.comparisonsOfTheFirstDegree(9, 21, 48))
    print(comparsion.comparisonsOfTheFirstDegree(5, 19, 33))
    print(comparsion.comparisonsOfTheFirstDegree(3, 19, 34))


def outputQuadraticResides():
    quadraticResidues = QuadraticResidues()
    # print(quadraticResidues.symbolLegandre(1,5))
    # print(quadraticResidues.symbolLegandre(4,14))
    # print(quadraticResidues.symbolLegandre(5, 10))
    # print(quadraticResidues.symbolLegandre(7, 33))
    # print(quadraticResidues.symbolLegandre(4, 7))
    # print(quadraticResidues.symbolLegandre(5, 11))
    # print(quadraticResidues.calculateQuadraticResidues(8, 17))
    # print(quadraticResidues.calculateQuadraticResidues(5, 11))
    # print(quadraticResidues.calculateQuadraticResidues(86, 125))
    # print(quadraticResidues.calculateQuadraticResidues(33,64))
    print(quadraticResidues.calculateQuadraticResidues(20, 47))


def outputWorkCalcFieldGalue2():
    # calcPolynom = CalculatorPolynomGalua([8,4,3,1,0])
    # print(format(calcPolynom.multPolynomsInBite([5,2,1],[7,4,3,2,1]),'b'))
    # calcPolynom = CalculatorPolynomGalua([3,2,0])
    # print(bin(calcPolynom.multPolynomsInBite([2,1,0],[2,1,0])))
    # calcPolynom = CalculatorPolynomGalua([3,1,0])
    # print(calcPolynom.multmodPolynom([2, 0], [2, 1, 0]))
    # calcPolynom = CalculatorPolynomGalua([4, 3, 0])
    # print(calcPolynom.GCDPolynom([5, 0], [3, 2, 1, 0]))
    # print(calcPolynom.upPolynomByDegree([5, 0], 2))
    # print(calcPolynom.createTableMultGalua())
    calculatorFieldGalua2 = CalculatorPolynomGalua()
    calculatorFieldGalua2.runCalculator()






if __name__ == '__main__':
    # outputQuadraticResides()
    # outputWorkCalcFieldGalue2()
    print(pollardP1Factorization(57247159, 8))
    num1 = pollardP1Factorization(483, int(math.sqrt(483))+1)
    num2 = 483 / num1
    print(483,"=>",num1,num2, f"B={int(math.sqrt(483))+1}")
    num1 = pollardP1Factorization(1207, int(math.sqrt(1207)) + 1)
    num2 = 1207 / num1
    print(1207,"=>",num1, num2,f"B={int(math.sqrt(1207))+1}")
    num1 = pollardP1Factorization(561, int(math.sqrt(561)) + 1)
    num2 = 561 / num1
    print(561,"=>",num1, num2,f"B={int(math.sqrt(561))+1}")
    num1 = pollardP1Factorization(1219, int(math.sqrt(1219)) + 1)
    num2 = 1219 / num1
    print(1219,"=>",num1, num2,f"B={int(math.sqrt(1219))+1}")
