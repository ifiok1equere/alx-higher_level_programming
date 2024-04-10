#!/usr/bin/python3
""" This module describes a function that uses numpy """


def lazy_matrix_mul(m_a, m_b):
    import numpy as np
    """
    This function uses numpy to operate
    on two matrices by computing their product

    Args:
        m_a: matrix 1
        m_b: matrix 2

    Return:
        New matrix that is a result of the product
    """

    return (np.dot(m_a, m_b))
