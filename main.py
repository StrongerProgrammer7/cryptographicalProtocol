from ComparisonsOfTheFirstDegree import ComparisonsOfTheFirstDegree
from QuadraticResidues import QuadraticResidues
from CalculatorPolynom import CalculatorPolynomGalua

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
    print(quadraticResidues.calculateQuadraticResidues(4, 21))

if __name__ == '__main__':
    calcPolynom = CalculatorPolynomGalua([8,4,3,1,0])
    calcPolynom.multPolynomsInBite([5,2,1],[7,4,3,2,1])




