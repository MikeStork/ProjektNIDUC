def bitErrorRateValue(bit_seq1, bit_seq2):
    # Sprawdzamy, czy długości sekwencji są równe
    if len(bit_seq1) != len(bit_seq2):
        raise ValueError("Bit sequences must be of equal length.")

    # Licznik błędów
    errors = 0

    # Iteracja po bitach obu sekwencji i porównanie ich
    for b1, b2 in zip(bit_seq1, bit_seq2):
        if b1 != b2:
            errors += 1

    return errors


def bitErrorRate(bit_seq1, bit_seq2):
    if len(bit_seq1) != len(bit_seq2):
        raise ValueError("Bit sequences must be of equal length.")

    return bitErrorRateValue(bit_seq1, bit_seq2) / len(bit_seq1)


if __name__ == '__main__':
    bit_seq1 = "11110000"
    bit_seq2 = "00011111"
    print(bitErrorRateValue(bit_seq1, bit_seq2))
    print("\n")
    print(bitErrorRate(bit_seq1, bit_seq2))
