from MyMath import MyMath


class QuadraticResidues(MyMath):

    def _symbolJacobi(self, a, p):
        factors = MyMath.factorIntoPrimeFactors(p)
        print(f"factors for {p}")
        mult = 1
        for elem in factors:
            mult *= self.symbolLegandre(a, elem)
            mult = self._reverseClassDeduction(mult,elem)
            print(f"{a}/{elem} = {mult}; ")
            if mult == 0:
                return 0
        return mult

    def symbolLegandre(self, a, p):
        print(f"Find symbol legandre ({a}/{p})")
        a,p = self._divToNOD(a, p)
        if a > p:
            a = a % p
        match a:
            case 0:
                return 0
            case 1:
                return 1
            case 2:
                return pow(-1, ((pow(p, 2) - 1) // 8))
            case -1:
                return pow(-1, (p - 1) // 2)

        if MyMath.is_prime(p) and p % 2 == 1:
            print(f"{p} is prime and odd - execution Euler: a^((p-1)/2) mod p")
            return self._reverseClassDeduction(pow(a, (p - 1) // 2) % p,p)

        if MyMath.isOdd(a) and MyMath.isOdd(p) and MyMath.is_prime(a) and MyMath.is_prime(p):
            return self._reverseClassDeduction(self.symbolLegandre(p % a, a),p) * pow(-1, ((a - 1) * (p - 1)) / 4)

        print(f"Execution Jacobi so as {p} isn't prime and not odd")
        _, _, nod = MyMath.extendedEuclideanAlgorithm(a, p)

        if MyMath.isOdd(a) and MyMath.isOdd(p) and nod == 1:
            print(f"NOD({a},{p}) == 1 Execution Jacobi - Gauss ")
            return self._reverseClassDeduction(self.symbolLegandre(p % a, a),p) * pow(-1, ((a - 1) * (p - 1)) / 4)
        else:
            print(f"Execution Jacobi - let's factorize {p}")
            return self._symbolJacobi(a, p)

    def _divToNOD(self, a, b):
        _,_,nod = MyMath.extendedEuclideanAlgorithm(a,b)
        return a // nod, b // nod

    # Обратное число для класса вычетов 6 % 7 = - 1 % 7
    def _reverseClassDeduction(self,a,b):
        if a + 1 == b:
            return a - b
        return a
