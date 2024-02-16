
from ComparisonsOfTheFirstDegree import ComparisonsOfTheFirstDegree
from QuadraticResidues import QuadraticResidues


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

if __name__ == '__main__':
    quadraticResidues = QuadraticResidues()
    #print(quadraticResidues.symbolLegandre(12,3427))
    #print(quadraticResidues.symbolLegandre(4,14))
    #print(quadraticResidues.symbolLegandre(5, 10))
    #print(quadraticResidues.symbolLegandre(7, 33))
    #print(quadraticResidues.symbolLegandre(4, 7))
    #print(quadraticResidues.symbolLegandre(5, 11))
    #print(quadraticResidues.symbolLegandre(7, 13))
    print(quadraticResidues.symbolLegandre(12, 7))

