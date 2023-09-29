# 2-matrix_divided.txt

==============================
How to Use 2-matrix_divided.py
==============================

This module defines a matrix division function called `matrix_divided(matrix, div)`.

Usage
=====

The `matrix_divided(...)` function returns a new matrix that is a copy of the parameter `matrix` with all elements divided by `div`.

**Example 1: Dividing a matrix by an integer**

```python
>>> from 2-matrix_divided import matrix_divided
>>> matrix = [
...     [3, 6, 9],
...     [12, 15, 18]
... ]
>>> print(matrix_divided(matrix, 3))
[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
>>> matrix = [
...     [1, 2, 3],
...     [4, 5, 6]
... ]
>>> print(matrix_divided(matrix, 3))
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
>>> print(matrix)
[[1, 2, 3], [4, 5, 6]]
>>> matrix = [
...     [1.1, -2.2, 3.3],
...     [4.4, 5.5, -6.6]
... ]
>>> print(matrix_divided(matrix, 3))
[[0.37, -0.73, 1.1], [1.47, 1.83, -2.2]]
>>> matrix = [
...     [1, -2.2, 3, 4.4, 5],
...     [-6.6, 7.00, 8, 9.999, 10]
... ]
>>> print(matrix_divided(matrix, 3))
[[0.33, -0.73, 1.0, 1.47, 1.67], [-2.2, 2.33, 2.67, 3.33, 3.33]]
>>> matrix = "not a list"
>>> print(matrix_divided(matrix, 3))
TypeError: matrix must be a matrix (list of lists) of integers/floats
>>> matrix = None
>>> print(matrix_divided(matrix, 3))
TypeError: matrix must be a matrix (list of lists) of integers/floats
>>> matrix = []
>>> print(matrix_divided(matrix, 3))
TypeError: matrix must be a matrix (list of lists) of integers/floats
>>> matrix = [
...     [1, 2, 3],
...     [4, "not a number", 6]
... ]
>>> print(matrix_divided(matrix, 3))
TypeError: matrix must be a matrix (list of lists) of integers/floats
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7]
... ]
>>> print(matrix_divided(matrix, 3))
TypeError: Each row of the matrix must have the same size
>>> matrix = [
...     [1, 2, 3],
...     [4, 5, 6]
... ]
>>> print(matrix_divided(matrix, "not a number"))
TypeError: div must be a number
>>> print(matrix_divided(matrix, None))
TypeError: div must be a number
>>> print(matrix_divided(matrix, 0))
ZeroDivisionError: division by zero

