import hashlib
def getChecksumMD5(data:str)->str:
    return hashlib.md5(data.encode()).hexdigest()

def getChecksumSHA256(data:str)->str:
    return hashlib.sha256(data.encode()).hexdigest()

def getChecksumSHA512(data:str)->str:
    return hashlib.sha512(data.encode()).hexdigest()

def getChecksumBlake2b(data:str)->str:
    return hashlib.blake2b(data.encode()).hexdigest()

def getChecksumPolynomial(data:str, coefficients: list[int])->str:
    data = data.lower()
    hash_value = 0
    for char in data:
        char_value = ord(char)
        for i in range(len(coefficients)):
            hash_value += coefficients[i] * (char_value ** (len(coefficients) - i))
    return hex(hash_value)

