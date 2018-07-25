import contracts
import numpy


@contracts.contract
def matrix_mult(a, b):
    """
    Multiplies two matrix
    :param a: The first matrix. 2D array
    :type a: array[MxN], M>0, N>0

    :param b: The second matrix. 2D array
              of compatible dimensions
    :type b: array[NxP], P>0
    :return: Returns array
    :rtype: array[MxP]
    """
    return numpy.dot(a, b)
