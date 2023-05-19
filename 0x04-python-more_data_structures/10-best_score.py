#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    score = list(a_dictionary.values())
    for key,value in a_dictionary.items():
        for i in score:
            if value > i:
                best_scorer = key
    return best_scorer
