#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Bowling score."""


def throw_value(i):
    """Return value for single character."""
    if i == '-':
        return 0
    if i == 'X':
        return 10
    return int(i)


def bowling(scorecard):
    """Calculate the score."""
    scorecard = scorecard.replace(' ', '')

    score = 0
    frame = 0
    throw = 0
    for i in range(len(scorecard)):
        c = scorecard[i]
        throw += 1
        if throw == 2:
            throw = 0
            frame += 1
        if c == "/":
            score += 10 - throw_value(scorecard[i-1]) + \
                throw_value(scorecard[i+1])
        elif c == "X":
            throw = 0
            frame += 1
            if scorecard[i+2] != '/':
                score += 10 + throw_value(scorecard[i+1]) + \
                    throw_value(scorecard[i+2])
            else:
                score += 20
        else:
            score += throw_value(c)
        if frame == 10:
            break
    return score


if __name__ == "__main__":
    import nose
    nose.main()
