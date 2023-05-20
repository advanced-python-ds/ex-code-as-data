import numpy as np


def func_of_func(func: callable) -> None:
    print(func.__module__)
    print(func.__name__)
    print(func(range(1, 11)))


if __name__ == "__main__":
    func_of_func(np.sum)
