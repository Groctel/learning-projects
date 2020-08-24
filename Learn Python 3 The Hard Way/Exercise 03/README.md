# Exercise 03

**A quick introduction to math.**

## Running this program

```sh
python3 ex3.py
```

## What I did

I wrote some `print` statements containing arithmetic and logic operations, which were printed with the text strings.

## What I learned

Python uses the following operators for doing arithmetic and logic operations:

| **Operator** | **Description**                                                                 |
| :----------: | ------------------------------------------------------------------------------- |
| `+`          | Adds two numbers.                                                               |
| `-`          | Substracts the number at the right from the one at the left.                    |
| `*`          | Multiples two numbers.                                                          |
| `/`          | Divides the number at the left by the one at the right.                         |
| `%`          | Returns the modulus from the integer division of two numbers.                   |
| `<`          | Checks if the number at the left is smaller than the one at the right.          |
| `>`          | Checks if the number at the left is greater than the one at the right.          |
| `<=`         | Checks if the number at the left is smaller or equal than the one at the right. |
| `>=`         | Checks if the number at the left is greater or equal than the one at the right. |

These operators have their [precedence rules](https://docs.python.org/3/reference/expressions.html#operator-precedence) and the `/` automatically casts the result to a floating point number.
When showing these results, `print` can cast both numeric and boolean values to strings, showing `True` or `False` for the latter instead of `1` and `0` like in other languages.
