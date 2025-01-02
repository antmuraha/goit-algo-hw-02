import random


def generate_unique_random_numbers(count):
    """
    Generates a list of unique random numbers within a specified range.
    """
    start = 0
    end = count
    return random.sample(range(start, end + 1), count)
