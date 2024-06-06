import hashlib


def getChecksumMD5(data: str) -> str:
    checksum = hashlib.md5(data.encode()).hexdigest()
    return bin(int(checksum, 16))[2:].zfill(128)


def getChecksumSHA256(data: str) -> str:
    checksum = hashlib.sha256(data.encode()).hexdigest()
    return bin(int(checksum, 16))[2:].zfill(256)


def getChecksumSHA512(data: str) -> str:
    checksum = hashlib.sha512(data.encode()).hexdigest()
    return bin(int(checksum, 16))[2:].zfill(512)


def getChecksumBlake2b(data: str) -> str:
    checksum = hashlib.blake2b(data.encode()).hexdigest()
    return bin(int(checksum, 16))[2:].zfill(256)


def crc_remainder(
    input_bitstring: str, polynomial_bitstring: str, initial_filler: str
) -> str:
    """Calculate the CRC remainder of a string of bits using a chosen polynomial.
    initial_filler should be '1' or '0'.
    """
    polynomial_bitstring = polynomial_bitstring.lstrip("0")
    len_input = len(input_bitstring)
    initial_padding = (len(polynomial_bitstring) - 1) * initial_filler
    input_padded_array = list(input_bitstring + initial_padding)
    while "1" in input_padded_array[:len_input]:
        cur_shift = input_padded_array.index("1")
        for i in range(len(polynomial_bitstring)):
            input_padded_array[cur_shift + i] = str(
                int(polynomial_bitstring[i] != input_padded_array[cur_shift + i])
            )
    return "".join(input_padded_array)[len_input:]


def crc_check(
    input_bitstring: str, polynomial_bitstring: str, check_value: str
) -> bool:
    """Calculate the CRC check of a string of bits using a chosen polynomial."""
    polynomial_bitstring = polynomial_bitstring.lstrip("0")
    len_input = len(input_bitstring)
    initial_padding = check_value
    input_padded_array = list(input_bitstring + initial_padding)
    while "1" in input_padded_array[:len_input]:
        cur_shift = input_padded_array.index("1")
        for i in range(len(polynomial_bitstring)):
            input_padded_array[cur_shift + i] = str(
                int(polynomial_bitstring[i] != input_padded_array[cur_shift + i])
            )
    return "1" not in "".join(input_padded_array)[len_input:]


def ParityBit(data: str) -> str:
    return crc_remainder(data, "11", "0")


def CRC8(data: str) -> str:
    return crc_remainder(data, "110100111", "0")


def CRC16(data: str) -> str:
    return crc_remainder(data, "11000000000000101", "0")


def CRC32(data: str) -> str:
    return crc_remainder(data, "100000100110000010001110110110111", "0")


print(ParityBit("101"))
