from ChineseRemainderTheorem import ChineseRemainderTheorem
from MyMath import MyMath


class QuadraticResidues(MyMath):
    chineseRemainder = ChineseRemainderTheorem()
    max_iteration = 100000

    def __init__(self, showStep=True):
        self.showStep = showStep

    def _symbolJacobi(self, a, p):
        factors = MyMath.factorIntoPrimeFactors(p)
        print(f"Find factors for {p}") if self.showStep is True else None
        mult = 1
        if self._isAllDivSame(factors):
            return self._calculateSymbolJacobi(a, factors[0])

        for elem in factors:
            mult = self._calculateSymbolJacobi(a, elem)

            print(f"{a}/{elem} = {mult}; ") if self.showStep is True else None
            if mult == 0:
                return 0
        return mult

    def _calculateSymbolJacobi(self, a, elem):
        mult = 1
        if a > elem:
            a = a % elem
        mult *= self.symbolLegandre(a, elem)
        mult = self._reverseClassDeduction(mult, elem)
        return mult

    def symbolLegandre(self, a, p):
        print(f"Find symbol legandre ({a}/{p})") if self.showStep is True else None
        a, p = self._divNumberToNOD(a, p)
        a = a % p
        resultProperties = self._calcPropertiesLegandre(a, p)
        if resultProperties is not None:
            return resultProperties

        if MyMath.is_prime(p) and p % 2 == 1:
            print(f"{p} is prime and odd - execution Euler: a^((p-1)/2) mod p") if self.showStep is True else None
            return self._reverseClassDeduction(pow(a, (p - 1) // 2) % p, p)

        _, _, nod = MyMath.extendedEuclideanAlgorithm(a, p, self.showStep)
        if MyMath.isOdd(a) and MyMath.isOdd(p) and ((MyMath.is_prime(a) and MyMath.is_prime(p)) or nod == 1):
            return self._reverseClassDeduction(self.symbolLegandre(p % a, a), p) * pow(-1, ((a - 1) * (p - 1)) / 4)

        print(f"Execution Jacobi - so as {p} isn't prime let's factorize {p}") if self.showStep is True else None
        return self._symbolJacobi(a, p)


    def _calcPropertiesLegandre(self, a, p):
        match a:
            case 0:
                return 0
            case 1:
                return 1
            case 2:
                return pow(-1, ((pow(p, 2) - 1) // 8))
            case -1:
                return pow(-1, (p - 1) // 2)
        return None

    # GET = p = 2^h * k + 2^(h-1) + 1 : return h,k
    def _getDegreeTwoAndFactorForPrimeNumber(self, a, p):
        if not MyMath.is_prime(p):
            print("P is not prime, you can't use factorization by 2") if self.showStep is True else None
            return -1
        # 2^h*k+2^(h-1)+1
        # 2^2 * 2 + 2 + 1 = 4 * 2 + 3
        # 8 + 3 = 11 => h=2 k=2
        # z= [0,0]
        # 2^(z(2k+1))*5^(k+1) mod 11 => 2^0 + 5^3 mod 11
        # 125 mod 11 = 4 mod 11
        k = a
        min_k = a
        h = 1
        output = ""
        while k > 0:
            result = pow(2, h) * k + 1

            if result == p:
                output = output + "2^" + str(h) + " * " + str(k) + " + 1="
                h += 1
            if (pow(2, h) * k + pow(2, h - 1) + 1) == p:
                min_k = k
                output = output + "2^" + str(h) + " * " + str(k) + " + " + str(2) + "^" + str(h-1) +" + 1 ="
            if k % 2 == 0:
                k = k // 2
            else:
                k -= 1

        print(output, f"{p}") if self.showStep is True else None

        if pow(2, h) * k + (pow(2, h - 1) + 1) == p or (pow(2, h) * min_k + pow(2, h - 1) + 1) == p:
            return h, min_k
        else:
            return None, None

    def calculateQuadraticResidues(self, a, p):
        print(f"calculate x^2 = {a} mod {p}")
        a = a % p
        if a == 1:
            print("Wow! a = 1 , we have solution +-1 mod any")
            return [1]

        if not MyMath.isOdd(p):
            return self._calcQuadraticResiduesWherePisEven(a, p)

        symbolLegandre = self.symbolLegandre(a, p)


        match symbolLegandre:
            case 1:
                print(f"Have 2 solution +- L={a}/{p}={symbolLegandre}")
            case -1:
                print(f" Symbol legandre {a}/{p} = -1 ====> not solution")
                return None
            case 0:
                print(f"Have 1 solution: L={a}/{p}={symbolLegandre}")

        if MyMath.is_prime(p):
            print(f"{p} is prime") if self.showStep is True else None
            h, k = self._getDegreeTwoAndFactorForPrimeNumber(a, p)
            if h is not None:
                return self._solutionPairsCandidate(a, p, h, k)
            else:
                print("Sorry,finding is difficult, accept range to 100000")
                return self._searchWithIteration(a,p)
        else:
            factors = self.factorIntoPrimeFactors(p)
            print(f"{p} is not prime", [elem for elem in factors]) if self.showStep is True else None
            if self._isAllDivSame(factors):
                print(f"We have all div same for {p}") if self.showStep is True else None
                result = self.calculateQuadraticResidues(a % factors[0], factors[0])
                print(
                    f"Solution: x^2={a} mod {factors[0]} ===> x=+-{result[0]} mod {factors[0]}  ({result[0]}+{factors[0]}t)") if self.showStep is True else None
                result = self._calculateT(factors,  a,[result[0], factors[0]])
                print(f"Solution: x=+-({result[0]} mod {p} )")
                return [result[0]]
            else:
                _, _, nod = MyMath.extendedEuclideanAlgorithm(a, p, False)
                return self._solutionWithChineseTheorem(a,p,factors) if nod == 1 else None

    def _calcQuadraticResiduesWherePisEven(self, a, p):
        if not MyMath.numberIsPowerTwo(p):
            return None
        print("Our mod is power two") if self.showStep is True else None
        alfa = MyMath.findPowerTwo(p)
        if alfa == 1:
            print("We have on solution: x=1 mod 2")
            return [1]
        elif alfa == 2:
            print("We have two solutions: x=+-1 mod 4") if self.showStep is True else None
            return [1]

        print(f"alfa > 3, solution: if {a} = 1 mod 8") if self.showStep is True else None
        if a % 8 == 1:
            print(f"{a} = 1 mod 8 ===> have 4 solutions  => x=+-(1+4t)") if self.showStep is True else None
            if alfa == 3:
                print("We have solution: +-1 mod 8 and +-3 mod 8")
                return [1, 3]
            factors = [8]
            for i in range(3, alfa):
                factors.append(2)
            x = [1,4]
            #x = self._bodyCalculateT(a, factors[0],[1, 4])
            x = self._calculateT(factors, a, x)
            x[1] = x[1] + x[0]
            print(f"First solutions: +-({x[0]} mod {p}) second solutions: +-({x[1]} mod {p})")
            return x
        return None

    def _calculateT(self, factors, a, x):
        for i in range(1, len(factors)):
            factors[i] = factors[i - 1] * factors[i]
            print(f"Iteration : {factors[i]}") if self.showStep is True else None
            x = self._bodyCalculateT(a, factors[i],x)
        return x

    def _bodyCalculateT(self, a, p, x):
        temp = a % p
        print(
            f"({x[0]}+{x[1]}t)^2={x[0] * x[0]}+2*{x[0]}*{x[1]}t*{x[1] * x[1]}t^2"
            f"= {temp} mod {p}") if self.showStep is True else None
        temp -= x[0] * x[0]
        t = 2 * x[0] * x[1]
        if temp != 0:
            [temp, t, p] = self._divArrayToNOD([temp, t, p])
        else:
            t, p = self._divNumberToNOD(t, p)

        t = t % p
        t = temp // t
        print(f"result = {t} mod {p}  ({t}+{p}t)") if self.showStep is True else None
        print(f"xprev = {x[0]} + {x[1]}t")
        x[0] = x[0] + x[1] * t
        x[1] = x[1] * p
        print(f"x = {x[0]} + {x[1]}t") if self.showStep is True else None
        return x

    def _solutionPairsCandidate(self, a, p, h, k):
        print(f"pairs of candidate solutions: 2^{h - 2}={pow(2, h - 2)}") if self.showStep is True else None
        print(f"Let's find some non-residue modulo {p}") if self.showStep is True else None

        someNonResidue = 0
        for i in range(2, p):
            if self.symbolLegandre(i, p) == -1:
                someNonResidue = i
                break
        print(f"We found nonResidue: {someNonResidue}") if self.showStep is True else None
        print(
            f"Using formuls x = {someNonResidue}^(z(2*{k}+1)) * {a}^({k}+1) mod {p}  z=0:{h - 2}") if self.showStep is True else None
        for i in range(0, pow(2, h - 2)):
            x = (pow(someNonResidue, i) * pow(a, k + 1)) % p
            print(f"x=(+-){someNonResidue}^{i} * {a}^{k + 1} mod {p} ===> {x} ") if self.showStep is True else None
            print(f"then: x^2={pow(x, 2) % p} mod {p}") if self.showStep is True else None
            if pow(x, 2) % p == a:
                print(f"We found solution: x=(+-){x} mod {p}")
                return [x]
        return None

    def _searchWithIteration(self,a,p):
        for i in range(2, self.max_iteration):
            x = i * i % p
            if x == a:
                print(f"We found solution with range: x^2={i * i} ===> x=(+-){i} mod {p}")
                return [i]
        print("Sorry, we can't find solution")
        return None

    def _solutionWithChineseTheorem(self,a,p,factors):
        print(f"NOD({a},{p}) = 1, have solutions") if self.showStep is True else None
        alfa = self._getSeniorDegree(factors)
        if alfa == 1:
            count_solutions = pow(2, len(factors))
        elif alfa == 2:
            count_solutions = pow(2, len(factors) + 1)
        else:
            count_solutions = pow(2, len(factors) + 2)
        print("All solutions: =" + str(count_solutions)) if self.showStep is True else None
        print("We have next system") if self.showStep is True else None
        self._printSystem(a, factors)
        system = []
        for elem in factors:
            results = self.calculateQuadraticResidues(count_solutions, elem)
            system.append([sum(results), elem])
        system = MyMath.generateSignVariations(system)
        print("Variations", system)
        solution = []
        for variation in system:
            result = self.chineseRemainder.calcChineseRemainder(variation)
            solution.append(result)
            print("Solution: " + str(result))
        return solution

    def _isAllDivSame(self, factors):
        total_div = factors[0]
        for div in factors:
            if div != total_div:
                return False
        return True

    def _getSeniorDegree(self, arr):
        max_power = 1
        arr = sorted(arr)
        for i in range(len(arr)):
            power = 1
            for j in range(i + 1, len(arr)):
                if arr[i] == arr[j]:
                    power += 1
                if arr[i] != arr[j]:
                    break
            i = j - 1
            if power > max_power:
                max_power = power
        return max_power

    def _divNumberToNOD(self, a, b):
        _, _, nod = MyMath.extendedEuclideanAlgorithm(a, b, False)
        return a // nod, b // nod

    def _divArrayToNOD(self, arr):
        nod = MyMath.gcdForArrayNumbers(arr)
        if nod == 0:
            return arr
        for i in range(len(arr)):
            arr[i] = arr[i] // nod
        return arr

    # Обратное число для класса вычетов 6 % 7 = - 1 % 7
    def _reverseClassDeduction(self, a, b):
        if a + 1 == b:
            return a - b
        return a

    def _printSystem(self,a,elems):
        for elem in elems:
            print(f"x^2={a} mod {elem}")