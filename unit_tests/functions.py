from typing import Union

def divide(divident: Union[int, float], divisor: Union[int, float]):
    return divident/ divisor

def multiply(*args: Union[int, float]):
    if len(args) == 0:
        raise ValueError("At least one value should be pass")

    total=1
    for arg in args:
        total *= arg

    return total


