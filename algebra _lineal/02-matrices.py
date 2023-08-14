from typing import Callable
from typing import Tuple
from typing import List

Matrix = List[List[float]]
Vector = List[float]

A = [[1, 2, 3],
     [4, 5, 6]]


def shape(A: Matrix) -> Tuple[int, int]:
    """devuelve las dimensiones de la matriz"""
    num_rows = len(A)
    num_columns = len(A[0]) if A else 0
    return num_rows, num_columns


assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)


def get_row(A: Matrix, n: int) -> Vector:
    """Devuelve la fila enésima de la matriz A como un vector"""
    s = shape(A)
    assert n <= s[0], "La fila solicitada excede las dimensiones de la matriz"
    return A[n]


assert get_row([[1, 2, 3], [4, 5, 6]], 1) == [4, 5, 6]


def get_column(A: Matrix, n: int) -> Vector:
    """Devuelve la fila enésima de la matriz A como un vector"""
    return [A_i[n] for A_i in A]


assert get_column([[1, 2, 3], [4, 5, 6]], 1) == [2, 5]


def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    """Devuelve una matriz de dimensiones num_rows x num_cols
    cuyos (i,j)-ésimos términos se introducen con entry_fn(i,j)"""
    return [[entry_fn(i, j)
             for j in range(num_cols)]
            for i in range(num_rows)]


def identity_matrix(n: int) -> Matrix:
    """Crea una matriz identidad con dimensiones n x n"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)


assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 1]]


#            user 0  1  2  3  4  5  6  7  8  9
#
friend_matrix = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # user 0
                 [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # user 1
                 [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # user 2
                 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],  # user 3
                 [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],  # user 4
                 [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],  # user 5
                 [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # user 6
                 [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # user 7
                 [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],  # user 8
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]  # user 9

assert friend_matrix[1][2] == 1, "0 and 2 are friends"
assert friend_matrix[0][8] == 0, "0 and 8 are not friends"
