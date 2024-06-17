import numpy as np

class GilbertElliotChannel:
    def __init__(
            self, 
            error_prob_good: float, 
            error_prob_bad: float, 
            state_change_prob_good_to_bad: float,
            state_change_prob_bad_to_good: float
        ):
            self.error_prob_good = error_prob_good
            self.error_prob_bad = error_prob_bad
            self.state_change_prob_good_to_bad = state_change_prob_good_to_bad
            self.state_change_prob_bad_to_good = state_change_prob_bad_to_good
            self.state = 0  # 0 represents "good" state, 1 represents "bad" state

    def transmit(self, data: str) -> str:
        """
        For every bit in input signal, generate error with given probability.
        After that update channel state.
        """
        transmitted_data = ""
        for bit in data:
            error = self._generate_error()
            if error:
                if bit == "0":
                    transmitted_data += "1"
                elif bit == "1":
                    transmitted_data += "0"
            else:
                transmitted_data += bit
            self._update_state()
        return transmitted_data

    def _generate_error(self):
        if self.state == 0:
            return np.random.choice([0, 1], p=[1 - self.error_prob_good, self.error_prob_good])
        else:
            return np.random.choice([0, 1], p=[1 - self.error_prob_bad, self.error_prob_bad])

    def _update_state(self):
        if self.state == 0:
            self.state = np.random.choice([0, 1], p=[1 - self.state_change_prob_good_to_bad, self.state_change_prob_good_to_bad])
        else:
            self.state = np.random.choice([0, 1], p=[1 - self.state_change_prob_bad_to_good, self.state_change_prob_bad_to_good])