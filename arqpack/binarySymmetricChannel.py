from komm import BinarySymmetricChannel
import numpy as np
from typing import List

def createBSC(crossoverProbability: float) -> BinarySymmetricChannel:
    return BinarySymmetricChannel(crossover_probability=crossoverProbability)

def sendSignalThroughBSC(bsc: BinarySymmetricChannel, inputSignal: List[int]) -> List[int]:
    np.random.seed(1)
    outputSignal = bsc(inputSignal)
    return outputSignal