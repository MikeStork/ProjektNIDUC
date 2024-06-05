### DEPRECATED
# from komm import BinarySymmetricChannel
# import numpy as np
# from typing import List

# def createBSC(crossoverProbability: float) -> BinarySymmetricChannel:
#     return BinarySymmetricChannel(crossover_probability=crossoverProbability)

# def sendSignalThroughBSC(bsc: BinarySymmetricChannel, inputSignal: List[int]) -> List[int]:
#     np.random.seed(1)
#     outputSignal = bsc(inputSignal)
#     return outputSignal

### END DEPRECATED

import random

def binary_symmetric_channel(input_str:str, error_prob:float)->str:
    """
    Simulates a Binary Symmetric Channel (BSC) which flips each bit in the input string
    with a probability of error_prob.

    Parameters:
    input_str (str): The input string consisting of '0's and '1's.
    error_prob (float): The probability with which each bit is flipped.

    Returns:
    str: The output string after passing through the BSC.
    """
    output_str = ""
    
    for dany_bit in input_str:
        if random.random() < error_prob:
            # Flip the bit
            if(dany_bit == "0"):
                output_str+="1"
            else:
                output_str+="0"
        else:
            # Keep the bit the same
            output_str+=str(dany_bit)
    
    return output_str