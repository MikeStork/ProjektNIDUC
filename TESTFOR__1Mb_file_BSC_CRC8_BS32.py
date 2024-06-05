import komm
import arqpack.binarySymmetricChannel as bscpack
import arqpack.utility as util
import arqpack.checksums as checksums
from arqpack.bitErrorRate import bitErrorRate as ber
import numpy as np
import matplotlib.pyplot as plt

start = 0.020
stop = 0.2
step = 0.005

Propabilities = np.arange(start, stop, step)


Data_Ber = []
Data_Redundancy = []
Data_Propability = []

# Read and prepare the input signal
entry = util.getSignalFromFile("input/example.txt")
entry = entry.replace("\n", "").replace("\t", "").replace(" ", "")
signal = util.splitBinary(entry, 64)

for prop in Propabilities:
    # Initialize error and CRC bit counters
    error_bits = 0
    signalAfterTransmission = []
    signalWithCRC = []
    receivedWithoutCRC = []


    # Process each block
    for enc_block in signal:
        transmitted_correctly = False
        while not transmitted_correctly:
            crc = checksums.CRC8(enc_block)
            blockToSend = enc_block + crc
            transmitted_block = bscpack.binary_symmetric_channel(util.convertStringToArrayOfBits(blockToSend), prop)
            
            # received_block = ''.join(map(str, transmitted_block))
            received_block = transmitted_block
            received_data = received_block[:-8]
            received_crc = received_block[-8:]
            crc_check = ((checksums.CRC8(received_data)==received_crc))
        
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
    print(f"SIGNAL OF LENGTH:\t{len(inputed_data)}")
    print(f"BER:\t\t{ber(inputed_data, ''.join(receivedWithoutCRC))}")
    print(f"REDUNDANCY:\t{Redundancy}")

    #Data to display on graphs

    Data_Ber.append(ber(inputed_data, ''.join(receivedWithoutCRC)))
    Data_Propability.append(prop)
    Data_Redundancy.append(Redundancy)

    
with open("output/aaaBSC_64_CRC8.txt") as f:
    f.write(";".join(Data_Propability)+"\n")
    f.write(";".join(Data_Ber)+"\n")
    f.write(";".join(Data_Redundancy)+"\n")


# Plotting the data
plt.figure(figsize=(10, 6))

plt.plot(Propabilities, Data_Ber, label='BER', marker='o')
plt.plot(Propabilities, Data_Redundancy, label='Redundancy', marker='s')
plt.plot(Propabilities, Data_Propability, label='Probability', marker='^')

    

plt.xlabel('Probability')
plt.ylabel('Values')
plt.title('Changes in BER, Redundancy, and Probability')
plt.legend()
plt.grid(True)
plt.savefig('output/aaa1Mb_BSC_64_CRC8.png', format='png')
plt.show()
