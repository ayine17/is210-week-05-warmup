#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" module name defaults with a function which takes two parameters and return
    logical comparison of the two argruments.
"""


def defaults(my_required, my_optional=True):
    """a function which takes two parameters and return logical comparison.

    args:
        my_optional (bool): arg with a default value of True
        my_required (mixed):  arg with no default value

    returns:
        Return the logical comparison of the two argruments

    Examples:
        >>> defaults(True)
        True

        >>> defaults(True, False)
        False

        >>> defaults(False, False)
        True
        """

    return my_optional is my_required
