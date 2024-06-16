import komm
import arqpack.binarySymmetricChannel as bscpack
import arqpack.utility as util
import arqpack.checksums as checksums
from arqpack.bitErrorRate import bitErrorRate as ber
import numpy as np
import matplotlib.pyplot as plt

start = 0.0001
stop = 0.0100
step = 0.0050

filename = "BSC_128_CRC8_16_32__5MB"
Propabilities = np.arange(start, stop, step)
prop = 0.000001
Data_Ber = []
Data_Redundancy = []
Data_Propability = []
CRC_polynomials = [checksums.CRC16,checksums.CRC32]

print(CRC_polynomials[0]("10101010101010"))
# Read and prepare the input signal
entry = util.getSignalFromFile("input/example.txt")
entry = entry.replace("\n", "").replace("\t", "").replace(" ", "")
signal = util.splitBinary(entry, 128)

for currentCrc in CRC_polynomials:
    # Initialize error and CRC bit counters
    error_bits = 0
    signalAfterTransmission = []
    signalWithCRC = []
    receivedWithoutCRC = []


    # Process each block
    for enc_block in signal:
        transmitted_correctly = False
        while not transmitted_correctly:
            crc = currentCrc(enc_block)
            blockToSend = enc_block + crc
            transmitted_block = bscpack.binary_symmetric_channel(util.convertStringToArrayOfBits(blockToSend), prop)
            
            # received_block = ''.join(map(str, transmitted_block))
            received_block = transmitted_block
            received_data = received_block[:-8]
            received_crc = received_block[-8:]
            crc_check = ((currentCrc(received_data)==received_crc))
        
            if not crc_check:
                error_bits += len(received_block)
            else:
                transmitted_correctly = True
                signalWithCRC.append(blockToSend)
                signalAfterTransmission.append(received_block)
                receivedWithoutCRC.append(received_data)

    # Calculate inputed data, signals, and redundancy
    inputed_data = entry
    inputed_signal = ''.join(signalWithCRC)
    received_signal = ''.join(signalAfterTransmission)

    total_bits_transmitted = len(received_signal)
    Redundancy = total_bits_transmitted - len(inputed_signal)+error_bits

    # Print results
    print(f"Propability:\t{prop}")
    print(f"SIGNAL OF LENGTH:\t{len(inputed_data)}")
    print(f"BER:\t\t{ber(inputed_data, ''.join(receivedWithoutCRC))}")
    print(f"REDUNDANCY:\t{Redundancy}")

    #Data to display on graphs
##
    Data_Ber.append(ber(inputed_data, ''.join(receivedWithoutCRC)))
    Data_Propability.append(prop)
    Data_Redundancy.append(Redundancy)


with open("output/{filename}.txt", "w") as f:
    f.write(";".join([str(item) for item in CRC_polynomials])+"\n")
    f.write(";".join([str(item) for item in Data_Redundancy])+"\n")
    f.write(";".join([str(item) for item in Data_Ber])+"\n")


# Plotting the data
plt.figure(figsize=(10, 6))

plt.plot(CRC_polynomials, Data_Ber, label='BER', marker='o')
plt.plot(CRC_polynomials, Data_Redundancy, label='Redundancy', marker='s')
# plt.plot(Propabilities, Data_Propability, label='Probability', marker='^')

    

plt.xlabel('Probability')
plt.ylabel('Values')
plt.title('Changes in BER, Redundancy, and Probability')
plt.legend()
plt.grid(True)
plt.savefig('output/{filename}.png', format='png')
plt.show()
