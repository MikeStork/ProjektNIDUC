import random


def stringToBinary(s: str) -> str:
    """Convert a string to a binary string

    Args:
        s (str): String to convert

    Returns:
        str: Converted binary string
    """
    return "".join(format(ord(i), "08b") for i in s)


def binaryToString(s: str) -> str:
    """Convert a binary string to a string

    Args:
        s (str): Binary string to convert

    Returns:
        str: Converted string
    """
    return "".join(chr(int(s[i : i + 8], 2)) for i in range(0, len(s), 8))


def splitBinary(s: str, n: int) -> list:
    """Split a binary string into n-bit chunks

    Args:
        s (str): Binary string to split
        n (int): Number of bits per chunk

    Returns:
        list: List of n-bit chunks
    """
    return [s[i : i + n] for i in range(0, len(s), n)]


def flipRandomBits(s: str, n: int) -> str:
    """Flip n random bits in a string

    Args:
        s (str): String to flip bits in
        n (int): Number of bits to flip

    Returns:
        str: a new string with n bits flipped
    """
    indices = random.sample(range(len(s)), n)
    s = list(s)
    for i in indices:
        s[i] = "0" if s[i] == "1" else "1"
    return "".join(s)