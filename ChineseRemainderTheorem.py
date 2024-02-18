from ComparisonsOfTheFirstDegree import ComparisonsOfTheFirstDegree
from MyMath import MyMath

class ChineseRemainderTheorem(MyMath):
    comparsion = ComparisonsOfTheFirstDegree()

    def calcChineseRemainder(self,system):
        m = []
        for elem in system:
            m.append(elem[1])
        nod = MyMath.gcd_recursiveForArray(m)
        if nod != 1:
            print("System not have solution: NOD(mods) != 1")
            return None
        M = 1
        for elem in m:
            M *= elem
        Mi = []
        Mireverse = []
        for elem in m:
            Mtemp = M // elem
            Mi.append(Mtemp)
            Mireverse.append(self.comparsion.comparisonsOfTheFirstDegree(Mtemp,1,elem))

        result = 0
        for i in range(len(system)):
            result+= system[i][0]*Mi[i]*Mireverse[i]
        return result % M
