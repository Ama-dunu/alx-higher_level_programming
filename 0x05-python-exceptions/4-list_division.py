#!/usr/bin/python3

def divide_lists_elementwise(list1, list2, length):
    """Divides two lists element by element.

    Args:
        list1 (list): The first list.
        list2 (list): The second list.
        length (int): The number of elements to divide.

    Returns:
        A new list of length 'length' containing the divisions.
    """
    result = []
    for i in range(length):
        try:
            division = list1[i] / list2[i]
        except TypeError:
            print("TypeError: Wrong type encountered")
            division = 0
        except ZeroDivisionError:
            print("ZeroDivisionError: Division by zero encountered")
            division = 0
        except IndexError:
            print("IndexError: Out of range")
            division = 0
        finally:
            result.append(division)
    return (result)
