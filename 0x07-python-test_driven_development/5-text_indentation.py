#!/usr/bin/python3
"""
    text_indentation: prints a text
    with 2 new lines afte
    each of these characters ('.,?:')
"""


def text_indentation(text):
    """print text with new conditions"""
    if type(text) is not str:
        raise TypeError('text must be a string')
    s = 0
    sc = chr
    for ch in text:
        if s == 0 and ch == " ":
            continue
        else:
            print(ch, end="")
            s = 1
    else:
        if (ch == "?" or ch == ":" or ch =="."):
            print(ch)
            print("")
            s = 0
        else:
            print(ch, end="")
