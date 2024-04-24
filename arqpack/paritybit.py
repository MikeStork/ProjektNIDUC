import utility


def encode(data: str) -> str:
    """Encode a string using a parity bit

    Args:
        data (str): String to encode

    Returns:
        str: Encoded string
    """
    data = utility.stringToBinary(data)
    parity = data.count("1") % 2
    return data + str(parity)


def decode(data: str) -> str:
    """Decode a string using a parity bit

    Args:
        data (str): String to decode

    Returns:
        str: Decoded string
    """
    data, parity = data[:-1], data[-1]
    if data.count("1") % 2 != int(parity):
        print("Error: Parity bit does not match")
    return utility.binaryToString(data)
