from typing import Dict, List, Any

import numpy as np
from pprint import pprint

FUNCS_NAMES = [
    "all",
    "alltrue",
    "amax",
    "amin",
    "any",
    "argmax",
    "argmin",
    "argsort",
    "around",
    "cumprod",
    "cumproduct",
    "cumsum",
    "mean",
    "ndim",
    "nonzero",
    "prod",
    "product",
    "ptp",
    "ravel",
    "round_",
    "shape",
    "size",
    "sometrue",
    "sort",
    "squeeze",
    "std",
    "sum",
    "transpose",
    "var",
]


def calculate(
    numbers: iter,
    *funcs: callable,
) -> Dict[str, Any]:
    """
    Calculate and store the results for a given range of numbers
    :param numbers: A range of numbers to execute the function on
    :param funcs: Functions to execute on the numbers
    :return: A dictionary with keys as function names and values as the results of the function
    """
    NotImplemented("Implement calculate function")


def main():
    """
    Given 29 numpy functions, calculate the results for the first 200 natural numbers
    """
    numbers = np.arange(1, 201)
    functions: List[callable] = [
        np.sum
    ]  # use a loop or a list comprehension to get all functions from the FUNCS_NAMES list
    data = calculate(numbers, *functions)
    return data


if __name__ == "__main__":
    # For your reference
    pprint(main())
