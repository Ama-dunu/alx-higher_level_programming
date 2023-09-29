# 5-text_indentation.txt

================================
How to Use 5-text_indentation.py
================================

This module defines a text-indentation function called `text_indentation(text)`.

Usage
=====

The `text_indentation(...)` function prints text with two new lines after each of the characters `.`, `?`, and `:`. No spaces are printed at the beginning of a line.

**Example 1: Adding new lines after punctuation**

```python
>>> from 5-text_indentation import text_indentation
>>> text_indentation("Hello?")
Hello?
<BLANKLINE>
>>> text_indentation("   Hi there.")
Hi there.
<BLANKLINE>
>>> text_indentation("          ")
>>> text_indentation("Hello.   ")
Hello.
<BLANKLINE>
>>> text_indentation("    Woah now.    This is messy.   ")
Woah now.
<BLANKLINE>
This is messy.
<BLANKLINE>
>>> text_indentation("No ending period, what bad grammar")
No ending period, what bad grammar
>>> text_indentation("Let's print a new-line! Here goes:\nPrinted.")
Let's print a new-line! Here goes:
<BLANKLINE>
<BLANKLINE>
Printed.
<BLANKLINE>
>>> text_indentation("\n\n\n We just printed three new lines.")
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
We just printed three new lines.
<BLANKLINE>
>>> text_indentation("A sneaky \n new line.")
A sneaky 
new line.
<BLANKLINE>
>>> text_indentation("Lorem ipsum dolor sit amet, consectetur adipiscing "
... "elit. Quonam modo? Utrum igitur tibi litteram videor an totas paginas "
... "commovere? Non autem hoc: igitur ne illud quidem. Fortasse id optimum, "
... "sed ubi illud: Plus semper voluptatis? Teneo, inquit, finem illi videri "
... "nihil dolere. Transfer idem ad modestiam vel temperantiam, quae est "
... "moderatio cupiditatum rationi oboediens. Si id dicis, vicimus. Inde "
... "sermone vario sex illa a Dipylo stadia confecimus. Sin aliud quid "
... "voles, postea. Quae animi affectio suum cuique tribuens atque hanc, "
... "quam dico. Utinam quidem dicerent alium alio beatiorem! Iam ruinas "
... "videres")
>>> text_indentation(7)
TypeError: text must be a string
>>> text_indentation({"one": 1, "two": 2})
TypeError: text must be a string
>>> text_indentation(None)
TypeError: text must be a string

