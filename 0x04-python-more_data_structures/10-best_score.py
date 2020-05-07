#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        score = max(a_dictionary.values())
        for person, i in a_dictionary.items():
            if i == score:
                return person
