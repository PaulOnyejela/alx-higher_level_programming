#!/usr/bin/python3

def multiple_returns(sentence):
    spann = len(sentence)
    if spann == 0:
        result = (0, None)
        return result
    else:
        res = (spann, sentence[0:1])
        return res
