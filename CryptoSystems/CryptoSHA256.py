from CryptoSystems.CryptoSystems import CryptoSystems




class CryptoSHA256(CryptoSystems):
    '''
    Example why h
    s_root = math.sqrt(2) # 1.4142135623730951
    fractions = math.modf(s_root)[0] # 0.41421356237309515
    fractions = hex(int(fractions * (2**32)))
    print(as_hex) #'0x6a09e667'
    '''

    '''
    Набор констант (k), который будет использоваться для подмешивания в хеш-дайджест,
     представляет собой первые 32 бита дробных частей кубических корней первых 64 простых чисел. 
     '''
    K = ['0x428a2f98', '0x71374491', '0xb5c0fbcf', '0xe9b5dba5', '0x3956c25b', '0x59f111f1', '0x923f82a4', '0xab1c5ed5',
         '0xd807aa98', '0x12835b01', '0x243185be', '0x550c7dc3', '0x72be5d74', '0x80deb1fe', '0x9bdc06a7', '0xc19bf174',
         '0xe49b69c1', '0xefbe4786', '0x0fc19dc6', '0x240ca1cc', '0x2de92c6f', '0x4a7484aa', '0x5cb0a9dc', '0x76f988da',
         '0x983e5152', '0xa831c66d', '0xb00327c8', '0xbf597fc7', '0xc6e00bf3', '0xd5a79147', '0x06ca6351', '0x14292967',
         '0x27b70a85', '0x2e1b2138', '0x4d2c6dfc', '0x53380d13', '0x650a7354', '0x766a0abb', '0x81c2c92e', '0x92722c85',
         '0xa2bfe8a1', '0xa81a664b', '0xc24b8b70', '0xc76c51a3', '0xd192e819', '0xd6990624', '0xf40e3585', '0x106aa070',
         '0x19a4c116', '0x1e376c08', '0x2748774c', '0x34b0bcb5', '0x391c0cb3', '0x4ed8aa4a', '0x5b9cca4f', '0x682e6ff3',
         '0x748f82ee', '0x78a5636f', '0x84c87814', '0x8cc70208', '0x90befffa', '0xa4506ceb', '0xbef9a3f7', '0xc67178f2']

    def __init__(self):
        super().__init__()
        self.h = ['0x6a09e667', '0xbb67ae85', '0x3c6ef372', '0xa54ff53a', '0x510e527f', '0x9b05688c', '0x1f83d9ab',
                  '0x5be0cd19']

    def translate(self, message):
        charcodes = [ord(c) for c in message]  # перевод в юникод
        # значения Юникода в 8-битные строки (удален двоичный индикатор)
        bytes = []
        for char in charcodes:
            bytes.append(bin(char)[2:].zfill(8))
        # 8-битные строки для списка битов как целых чисел
        bits = []
        for byte in bytes:
            for bit in byte:
                bits.append(int(bit))
        return bits

    def binToHex(self, value):
        # takes list of 32 bits and convert to string
        value = ''.join([str(x) for x in value])
        # create 4 bit chunks, and add bin-indicator(0b)
        binaries = []
        for d in range(0, len(value), 4):
            binaries.append('0b' + value[d:d + 4])
        # transform to hexadecimal and remove hex-indicator(0x)
        hexes = ''
        for b in binaries:
            hexes += hex(int(b, 2))[2:]
        return hexes

    def fillZeros(self, bits, length=8, endian='LE'):
        l = len(bits)
        if endian == 'LE':
            for i in range(l, length):
                bits.append(0)
        else:
            while l < length:
                bits.insert(0, 0)
                l = len(bits)
        return bits

    def chunker(self, bits, chunk_length=8):
        # делит список битов на нужные фрагменты байтов/слов,(32)
        # starting at LSB
        chunked = []
        for b in range(0, len(bits), chunk_length):
            chunked.append(bits[b:b + chunk_length])
        return chunked

    def initializer(self, values):
        # преобразовать шестнадцатеричную строку в двоичную строку Python (with cut bin indicator ('0b'))
        binaries = [bin(int(v, 16))[2:] for v in values]
        # преобразовать строковое представление Python в список из 32-битных списков
        words = []
        for binary in binaries:
            word = []
            for b in binary:
                word.append(int(b))
            words.append(self.fillZeros(word, 32, 'BE'))
        return words

    def preprocessMessage(self, message):
        # translate message into bits
        bits = self.translate(message)
        # message length
        lenMessage = len(bits)
        # get length in bits  of message (64 bit block)
        message_len = [int(b) for b in bin(lenMessage)[2:].zfill(64)] #[2:] - удалить 0b zfill добавить нули чтобы общая длина была 64
        # если длина меньше 448, в противном случае обрабатывайте блок отдельно
        # если ровно 448, то добавьте одну 1 и в сумме получите 1024, а если длиннее 448
        # создать длину, кратную 512–64 битам, для длины в конце сообщения (с прямым порядком байтов BE)
        if lenMessage < 448:
            # append single 1
            bits.append(1)
            # fill zeros little endian wise
            bits = self.fillZeros(bits, 448, 'LE')
            # add the 64 bits representing the length of the message
            bits = bits + message_len
            # return as list
            return [bits]
        elif 448 <= lenMessage <= 512:
            bits.append(1)
            # moves to next message block - total length = 1024
            bits = self.fillZeros(bits, 1024, 'LE')
            # replace the last 64 bits of the multiple of 512 with the original message length
            bits[-64:] = message_len
            # returns it in 512 bit chunks
            return self.chunker(bits, 512)
        else:
            bits.append(1)
            # loop until multiple of 512 + 64 bit message_len if message length exceeds 448 bits
            while (len(bits) + 64) % 512 != 0:
                bits.append(0)
            # add the 64 bits representing the length of the message
            bits = bits + message_len
            # returns it in 512 bit chunks
            return self.chunker(bits, 512)

    def sha256(self, message):
        k = self.initializer(self.K)
        h0, h1, h2, h3, h4, h5, h6, h7 = self.initializer(self.h)
        blocks = self.preprocessMessage(message)
        for block in blocks:
            w = self.chunker(block, 32)
            for _ in range(48):
                w.append(32 * [0])
            for i in range(16, 64):
                s0 = self.getXORZipArrays([self.cyclicShiftRight(w[i - 15], 7), self.cyclicShiftRight(w[i - 15], 18), self.shiftRight(w[i - 15], 3)])
                s1 = self.getXORZipArrays([self.cyclicShiftRight(w[i - 2], 17), self.cyclicShiftRight(w[i - 2], 19), self.shiftRight(w[i - 2], 10)])
                w[i] = self.sumBits(self.sumBits(self.sumBits(w[i - 16], s0), w[i - 7]), s1)
            a = h0
            b = h1
            c = h2
            d = h3
            e = h4
            f = h5
            g = h6
            h = h7
            for j in range(64):
                S1 = self.getXORZipArrays([self.cyclicShiftRight(e, 6), self.cyclicShiftRight(e, 11), self.cyclicShiftRight(e, 25)])
                ch = self.getXORZipArrays([self.getANDArray(e, f), self.getANDArray(self.getNotArray(e), g)])
                temp1 = self.sumBits(self.sumBits(self.sumBits(self.sumBits(h, S1), ch), k[j]), w[j])
                S0 = self.getXORZipArrays([self.cyclicShiftRight(a, 2), self.cyclicShiftRight(a, 13), self.cyclicShiftRight(a, 22)])
                m = self.getXORZipArrays([self.getANDArray(a, b), self.getANDArray(a, c), self.getANDArray(b, c)])
                temp2 = self.sumBits(S0, m)
                h = g
                g = f
                f = e
                e = self.sumBits(d, temp1)
                d = c
                c = b
                b = a
                a = self.sumBits(temp1, temp2)
            h0 = self.sumBits(h0, a)
            h1 = self.sumBits(h1, b)
            h2 = self.sumBits(h2, c)
            h3 = self.sumBits(h3, d)
            h4 = self.sumBits(h4, e)
            h5 = self.sumBits(h5, f)
            h6 = self.sumBits(h6, g)
            h7 = self.sumBits(h7, h)
        digest = ''
        for val in [h0, h1, h2, h3, h4, h5, h6, h7]:
            digest += self.binToHex(val)
        return digest
