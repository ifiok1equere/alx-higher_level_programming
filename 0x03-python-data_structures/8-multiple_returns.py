#!/usr/bin/python3


def multiple_returns(sentence):
    if len(sentence) == 0:
        length, char = 0, None
    else:
        length, char = len(sentence), sentence[0]
    tuple_ = length, char
    return (tuple_)
