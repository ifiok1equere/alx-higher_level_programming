#!/usr/bin/python3
""" This module describes a function that uses numpy """
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    This function uses numpy to operate
    on two matrices by computing their product

    Args:
        m_a: matrix 1
        m_b: matrix 2

    Return:
        New matrix that is a result of the product
    """

    return numpy.multiply(m_a, m_b)
