import arqpack.utility as util
import  arqpack.checksums as checksums
from arqpack.bitErrorRate import bitErrorRateValue as ber
import arqpack.gilbertElliotChannel as GEC

# Bad channel
error_prob_good: float = 0.000001 
error_prob_bad: float = 0.001
state_change_prob_good_to_bad: float = 0.1
state_change_prob_bad_to_good: float = 0.1

gec = GEC.GilbertElliotChannel(
    error_prob_good, 
    error_prob_bad,
    state_change_prob_good_to_bad, 
    state_change_prob_bad_to_good)

# Get bits from file
entry = util.getSignalFromFile("example.txt")
entry = entry.replace("\n","").replace("\t","").replace(" ","")

N = []
BER = []
REDUNDANCY = []
ROWNE = []
# Split signal into chunks of given size
for n in range(2, 128, 10):
    N.append(n)
    BER_sum = 0
    REDUNDANCY_sum = 0
    for z in range(10):
        signal = util.splitBinary(entry, n)
        how_many_blocks = len(signal)
        print(n, "number of blocks: " + str(how_many_blocks))

        # number_of_errors = 0
        block_counter = 0
        redundancy = 0

        # Calculate CRC for each chunk
        signal_with_crc = []
        for block in signal:
            checksum = checksums.ParityBit(block)
            signal_with_crc.append(block+checksum)
            redundancy += len(checksum)

        # Transmit part of the signal with calculated CRC.
        # On the receiver site check if the data is correct. If not retransmit the data.
        # Do it until the whole signal is transmitted correctly.
        signal_after_transmission = []
        for enc_block in signal_with_crc:
            print(block_counter)
            new_enc_block = gec.transmit(enc_block)
            # number_of_errors += ber(enc_block, new_enc_block)
            success = checksums.ParityBit(new_enc_block[:-1]) == new_enc_block[-1:]
            while success == False:
                new_enc_block = gec.transmit(enc_block)
                # number_of_errors += ber(enc_block, new_enc_block)
                redundancy += len(new_enc_block)
                success = checksums.ParityBit(new_enc_block[:-1]) == new_enc_block[-1:]
            block_counter += 1
            signal_after_transmission.append(new_enc_block)
        start = ''.join(signal_with_crc)
        end = ''.join(signal_after_transmission)
        number_of_errors = ber(start, end)
        BER_sum += number_of_errors/len(start)
        REDUNDANCY_sum += redundancy
        print(n, BER_sum, REDUNDANCY_sum)
    BER.append(BER_sum/10.0)
    # BER.append(BER_sum)
    REDUNDANCY.append(REDUNDANCY_sum/10)
    # REDUNDANCY.append(REDUNDANCY_sum)

with open("wyniki_ok/LEGANCKI-wynikiCRC1GBCdobry.txt", "w+") as f:
    for i in range(len(N)):
        f.write(f"{N[i]},{BER[i]},{REDUNDANCY[i]}\n")