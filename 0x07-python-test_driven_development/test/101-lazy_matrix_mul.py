# 101-lazy_matrix_mul.txt

===========================================
How to Use 101-lazy_matrix_mul.py
===========================================

This module defines a matrix multiplication function called `lazy_matrix_mul(m_a, m_b)`.

## Usage

The `lazy_matrix_mul(...)` function returns a new matrix representing the multiplication of `m_a` by `m_b`.

```python
>>> from __import__('101-lazy_matrix_mul').lazy_matrix_mul
>>> m_a = [
...     [1, 2],
...     [3, 4],
... ]
>>> m_b = m_a
>>> print(lazy_matrix_mul(m_a, m_b))
[[ 7 10]
 [15 22]]
>>> m_a = [
...     [1.2, 5.5, 6.2],
...     [4.66, 12.3, -9.2]
... ]
>>> m_b = [
...     [5.0, 3.3],
...     [-2.9, 4.4],
...     [7.2, 4.4]
... ]
>>> print(lazy_matrix_mul(m_a, m_b))
[[ 34.69   55.44 ]
 [-78.61   29.018]]
>>> print(lazy_matrix_mul(m_a))  # Raises TypeError
>>> print(lazy_matrix_mul())  # Raises TypeError
>>> m_a = [
...     [1, 2],
...     [3, 4],
... ]
>>> m_b = [
...     [1, 2],
...     [2, 3],
...     [4, 5]
... ]
>>> print(lazy_matrix_mul(m_a, m_b))  # Raises ValueError
>>> print(lazy_matrix_mul([[]], [[5, 6], [7, 8]]))  # Raises ValueError
>>> print(lazy_matrix_mul("not a list", [[1, 2]]))  # Raises ValueError
>>> print(lazy_matrix_mul([[1, "non-number"]], [[3, 4]]))  # Raises ValueError
>>> print(lazy_matrix_mul(None, None))  # Raises TypeError
>>> print(lazy_matrix_mul([1, 2], [[3, 4]]))  # Raises ValueError
>>> print(lazy_matrix_mul([[1, "non-number"]], [[{"a": 1}, 8.8]]))  # Raises ValueError/TypeError
>>> m_a = [
...     [1, 2],
...     [3, 4, 5]
... ]
>>> m_b = [
...     [1, 2],
...     [3, 4]
... ]
>>> print(lazy_matrix_mul(m_a, m_b))  # Raises ValueError

