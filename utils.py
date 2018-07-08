"""
Modifying builtin input functions
"""
import builtins
from typing import Iterator

SAMPLE_INPUTS: Iterator = None


def init(sample_inputs):
    """Init with sample input"""
    assign_inputs(sample_inputs)
    builtins.input = custom_input


def assign_inputs(sample_inputs):
    global SAMPLE_INPUTS
    SAMPLE_INPUTS = iter(filter(len, sample_inputs.split("\n")))


def custom_input(obj=None):
    if obj:
        print(obj)
    return next(SAMPLE_INPUTS, None)
