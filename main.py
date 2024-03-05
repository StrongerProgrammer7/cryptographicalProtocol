import math
from ComparisonsOfTheFirstDegree import ComparisonsOfTheFirstDegree
from CryptoSystems.CryptoDES import CryptoDES
from CryptoSystems.CryptoDSS import CryptoDSS
from CryptoSystems.CryptoSHA256 import CryptoSHA256
from MyMath import MyMath
from QuadraticResidues import QuadraticResidues
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

def calculatePolardoPrint(n):
    num1 = MyMath.pollardRHOFactorization(n)
    num2 = n / num1
    print(n, "=>", num1, num2)

def calculatePolardoP_1():
    print(MyMath.pollardP1Factorization(57247159, 8))
    num1 = MyMath.pollardP1Factorization(483, int(math.sqrt(483)) + 1)
    num2 = 483 / num1
    print(483, "=>", num1, num2, f"B={int(math.sqrt(483)) + 1}")

def workDESCrypto(message,keyLen):
    cryptosystemsCBC = CryptoDES("DES.CBC")
    cryptosystemsCFB = CryptoDES("DES.CFB")
    # Пример использования
    keyCBC = cryptosystemsCBC.generateKey(keyLen)
    keyCFB = cryptosystemsCFB.generateKey(keyLen)
    message_to_encrypt = message #

    # Шифрование
    encrypted_message = cryptosystemsCBC.encrypt_des(message_to_encrypt, keyCBC)
    print(f"Encrypted message: {encrypted_message.hex()}")

    # Расшифрование
    decrypted_message = cryptosystemsCBC.decrypt_des(encrypted_message, keyCBC)
    print(f"Decrypted message: {decrypted_message}")

    encrypted_message = cryptosystemsCFB.encrypt_des(message_to_encrypt, keyCFB)
    print(f"Encrypted message: {encrypted_message.hex()}")

    # Расшифрование
    decrypted_message = cryptosystemsCFB.decrypt_des(encrypted_message, keyCFB)
    print(f"Decrypted message: {decrypted_message}")

def workDSS():
    file_path = "./CryptoSystems/example.txt"
    cryptoDSS = CryptoDSS(file_path)
    cryptoDSS.generate_keypair()
    print("Public key" , cryptoDSS.public_key)
    print("Private key", cryptoDSS.private_key)
    signature = cryptoDSS.sign_file(cryptoDSS.private_key)
    print("Signature",signature)
    verificationResult = cryptoDSS.verify_signature(cryptoDSS.public_key,signature)
    print(verificationResult)


if __name__ == '__main__':
    # outputQuadraticResides()
    # outputWorkCalcFieldGalue2()
    #calculatePolardoP_1()
    #print(PollardRHOFactorization(434617))
    #workDESCrypto("Hello, DES CBC!",8)
    #workDSS()

    cryptoSHA256 = CryptoSHA256()
    print(cryptoSHA256.translate('XO'))
    print(cryptoSHA256.binToHex(cryptoSHA256.translate('XO')))
    message = "Hello SHA256"
    hash_example = cryptoSHA256.sha256(message)
    print('message: ',message," =====>", hash_example)
    print('70725d0f78cb0967c0e5171f733619712d239e28f2d279e4b3c3ed97f7456fa3' == hash_example)