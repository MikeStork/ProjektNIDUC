def bitErrorRate(bit_seq1, bit_seq2):
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
