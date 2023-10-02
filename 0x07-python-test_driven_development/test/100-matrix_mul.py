# 100-matrix_mul.txt

=========================================
How to Use the matrix_mul Function
=========================================

This module defines a matrix multiplication function called `matrix_mul(m_a, m_b)`.

## Usage

The `matrix_mul(...)` function returns a new matrix that represents the multiplication of `m_a` by `m_b`.

```python
>>> from __import__('100-matrix_mul').matrix_mul
>>> m_a = [
...     [1, 2],
...     [3, 4],
... ]
>>> m_b = m_a
>>> print(matrix_mul(m_a, m_b))
[[7, 10], [15, 22]]
>>> m_a = [
...     [1.2, 5.5, 6.2],
...     [4.66, 12.3, -9.2]
... ]
>>> m_b = [
...     [5.0, 3.3],
...     [-2.9, 4.4],
...     [7.2, 4.4]
... ]
>>> print(matrix_mul(m_a, m_b))
[[34.69, 55.44], [-78.61, 29.018]]
>>> m_a = [
...     [1, 2.2, 3.3, 4],
...     [5, 6, 7, 8.8],
... ]
>>> m_b = [
...     [1.1, 2, 3.3],
...     [4.0, 5.5, 6],
...     [7, 8, 9],
...     [10.01, 11, 12.3]
... ]
>>> print(matrix_mul(m_a, m_b))
[[73.04, 84.5, 95.4], [166.59, 195.8, 223.74]]
>>> print(matrix_mul())  # Raises TypeError
>>> m_a = [
...     [1, 2],
...     [3, 4],
... ]
>>> m_b = [
...     [1, 2],
...     [2, 3],
...     [4, 5]
... ]
>>> print(matrix_mul(m_a, m_b))  # Raises ValueError
>>> print(matrix_mul([], [[1, 2]]))  # Raises ValueError
>>> print(matrix_mul("not a list", [[1, 2]]))  # Raises TypeError
>>> print(matrix_mul([[1, "non-number"]], [[3, 4]]))  # Raises TypeError
>>> m_a = [
...     [1, 2],
...     [3, 4, 5]
... ]
>>> m_b = [
...     [1, 2],
...     [3, 4]
... ]
>>> print(matrix_mul(m_a, m_b))  # Raises TypeError
