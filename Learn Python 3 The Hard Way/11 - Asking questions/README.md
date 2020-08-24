# Exercise 11

**Asking Questions**

## Running this program

```sh
python3 ex11.py
```

## What I did

I created variables whose values were assigned from a string gotten trough `stdin`.

## What I learnt

Since Python is dynamically typed, `input()` defaults the data read to a string.
In order to get another data type (an integer, for example), a casting has to be done calling the data type's constructor that accepts a string as an argument:

```python
fpnum   = float(input())
integer = int(input())
```
