#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""a function with three parameters.
"""


def too_many_kittens(kittens, litterboxes, catfood):
    """ a function that takes three arguments and return bool.


    args:
        kittens (int): the number of kittens
        litterboxes (int): the number of available litterboxes
        catfood (bool): a boolean representing whether or not any catfood exists

    Returns:
        return a bool of the comparison of the three args


    Example
        >>> too_many_kittens(12, 12, False)
        True

        >>> too_many_kittens(13, 12, True)
        True

        >>> too_many_kittens(12, 13, True)
        False

        >>> too_many_kittens(12, 12, 1)
        False
    """

    return not (litterboxes >= kittens and catfood)
