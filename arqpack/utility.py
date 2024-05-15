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
def getSignalFromFile(filename: str)->str:
    with open("../input/"+filename,"r+") as f:
        return f.read().replace("\t","").replace("\n","").replace(" ","")
def writeSignalToFile(filename: str, signal: str) ->bool:
    try:
        with open("../output/"+filename, 'w') as file:
            file.write(signal)
        return True
    except Exception as e:
        print(f"Error occurred: {e}")
        return False
def checkIfCorrectFormOfSignal(signal:str) ->bool:
    for x in signal:
        if(x == "0" or x == "1"):
            continue
        else:
            return False
    return True    