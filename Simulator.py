import Distributions

START = 0


def get_expo(mean_value):
    arrival = START + Distributions.exponential(mean_value)
    return arrival


def get_uniform(lower_bound, upper_bound):
    return Distributions.uniform(lower_bound, (lower_bound + upper_bound) * 0.5) + Distributions.uniform(lower_bound, (
            lower_bound + upper_bound) * 0.5)


def get_feedback(beta):
    if Distributions.get_random() < beta:
        return True
    else:
        return False
