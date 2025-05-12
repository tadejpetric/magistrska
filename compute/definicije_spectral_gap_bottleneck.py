"""
The goal of the program is to find the spectral gap
(largest EV - 2nd largest EV) of a graph that
consists of two K_n connected together by an edge.
"""

import numpy as np
from numpy.typing import NDArray

def spectral_gap(A: NDArray[np.float64]) -> float:
    """
    Calculate the difference between the largest and second-largest eigenvalue of matrix A.

    Parameters:
    A (NDArray[np.float64]): A square matrix (numpy array)

    Returns:
    float: The spectral gap (difference between the largest and second-largest eigenvalue)
    """
    # Calculate the eigenvalues of the matrix A
    eigenvalues = np.linalg.eigvals(A)

    # Sort eigenvalues in descending order
    sorted_eigenvalues = np.sort(eigenvalues)[::-1]

    # Ensure the matrix has at least two distinct eigenvalues
    if len(sorted_eigenvalues) < 2:
        raise ValueError("Matrix must have at least two eigenvalues")

    # Return the difference between the largest and second-largest eigenvalue
    print(sorted_eigenvalues)
    return np.real(sorted_eigenvalues[0] - sorted_eigenvalues[1])


import numpy as np

def one_connection(n: int) -> np.ndarray:
    """
    Construct a 2n x 2n adjacency matrix for two K_n graphs connected by one edge.

    Parameters:
    n (int): The size of each K_n graph.

    Returns:
    np.ndarray: The 2n x 2n adjacency matrix.
    """
    # Initialize a 2n x 2n matrix of zeros
    A = np.zeros((2 * n, 2 * n), dtype=np.int32)
    
    # Fill the upper-left and lower-right blocks (complete graphs K_n)
    # Set all entries to 1, except the diagonal (which should remain 0)
    K_n = np.ones((n, n), dtype=np.int32) - np.eye(n, dtype=np.int32)
    
    # Place the upper-left and lower-right blocks in the matrix
    A[:n, :n] = K_n
    A[n:, n:] = K_n

    # Remove extra edges from Kns
    A[n-1, n-2] = 0
    A[n-2, n-1] = 0
    A[n, n+1] = 0
    A[n+1, n] = 0

    # Connect the two K_n graphs with two edges
    A[n-1, n] = 1   
    A[n-2, n+1] = 1
    A[n, n-1] = 1   
    A[n+1, n-2] = 1
    
    return A

n = 31

from utils import is_ramanujan
matrix = one_connection(10)
print(matrix)
print(spectral_gap(matrix))
print(is_ramanujan(matrix))
#for i in range(3, n):
#    matrix = one_connection(i)
#    gap = spectral_gap(matrix)
#    print(f"({i}, {gap})")
