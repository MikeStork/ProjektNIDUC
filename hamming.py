import utility


def encode(data: str) -> str:
    """Encode a string using Hamming(7,4) code

    Args:
        data (str): String to encode

    Returns:
        str: Encoded string
    """
    data = utility.stringToBinary(data)
    print(data)
    data = utility.splitBinary(data, 4)
    hamming = ""
    print(data)
    for chunk in data:
        p1 = int(chunk[0]) ^ int(chunk[1]) ^ int(chunk[3])
        p2 = int(chunk[0]) ^ int(chunk[2]) ^ int(chunk[3])
        p4 = int(chunk[1]) ^ int(chunk[2]) ^ int(chunk[3])
        hamming += (
            str(p1) + str(p2) + chunk[0] + str(p4) + chunk[1] + chunk[2] + chunk[3]
        )
    return hamming


def decode(data: str) -> str:
    """Decode a string using Hamming(7,4) code

    Args:
        data (str): Encoded string to decode

    Returns:
        str: Decoded string
    """
    data = utility.splitBinary(data, 7)
    decoded = ""
    for chunk in data:
        p1 = int(chunk[0]) ^ int(chunk[2]) ^ int(chunk[4]) ^ int(chunk[6])
        p2 = int(chunk[1]) ^ int(chunk[2]) ^ int(chunk[5]) ^ int(chunk[6])
        p4 = int(chunk[3]) ^ int(chunk[4]) ^ int(chunk[5]) ^ int(chunk[6])
        if p1 or p2 or p4:
            print("Error in byte: " + chunk)
        decoded += chunk[2] + chunk[4] + chunk[5] + chunk[6]
    decoded = utility.binaryToString(decoded)
    return decoded
