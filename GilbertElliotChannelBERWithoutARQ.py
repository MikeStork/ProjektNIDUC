import arqpack.utility as util
from arqpack.bitErrorRate import bitErrorRate as ber
import arqpack.gilbertElliotChannel as GEC
import numpy as np

error_prob_bad_range = [0.01, 0.001, 0.0001, 0.00001]

start = 0.1
stop = 0.5
step = 0.05
state_change_prob_good_to_bad_range = np.arange(start, stop, step)

start = 0.1
stop = 0.5
step = 0.05
state_change_prob_bad_to_good_range = np.arange(start, stop, step)

Combinations = []
BERs = []

entry = util.getSignalFromFile("example.txt")
entry = entry.replace("\n","").replace("\t","").replace(" ","")
counter = 0
for error_prob_bad in error_prob_bad_range:
        for state_change_prob_good_to_bad in state_change_prob_good_to_bad_range:
            for state_change_prob_bad_to_good in state_change_prob_bad_to_good_range:
                print(counter)
                t = (error_prob_bad, 0.000001, state_change_prob_good_to_bad, state_change_prob_bad_to_good)
                Combinations.append(t)

                channel = GEC.GilbertElliotChannel(
                    0.000001, 
                    error_prob_bad, 
                    state_change_prob_good_to_bad,
                    state_change_prob_bad_to_good
                )
                signal_after_transmission = channel.transmit(entry)
                b = ber(entry, signal_after_transmission)
                print(t, b)
                BERs.append(b)
                counter += 1

with open("wynikiGECBER.txt", "w+") as f:
    for i in range(len(Combinations)):
        c = Combinations[i]
        b = BERs[i]
        f.write(f"{c[0]},{c[1]},{c[2]},{c[3]},{b}\n")