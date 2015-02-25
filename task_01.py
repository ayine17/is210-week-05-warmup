#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean
"""


def know_what_i_mean(wink, numwink=2):
    """ a function that concat 2 strings repeated numwink times with commas.

    args:
        wink (str): string arg to be repeat according to int arg numwink
        numwink=2 (int): arg to be used to repeat the string and the string:
                         default: 2

    return
        str: string argrument repeat and concatentated with commas and string
             nudges repeat by nunmink arg

    Example:
        >> wink='time'
        >>>know_what_i_mean(wink, numwink=2)
        'Know what I mean? timetime, nudge nudge'
    """

    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
