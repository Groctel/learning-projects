# Exercise 23

**Strings, Bytes, and Character Encodings**

## Running this program

```sh
python3 ex23.py utf-8 strict
```

## What I did

I created a program that reads a file line by line with `readline` and performed the following operations with it in `print_line`:

- I used `strip` to remove the trailing linefeed character.
- I used `encode` to extract the bytes that form the line string.
- I used `decode` to transform the string of bytes into a literal string.

To do this, I specified both hardcoded and in `argv` that the encoding standard should be `utf-8` and passed the `encode` and `decode` functions an error handling method of `'strict'`, that raises an error on failure.
This error method is the default.

Since loops haven't been introduced yet, the `main` function is called recursively.

## What I learnt

Python objects can return `true` or `false` depending on a defined function.
For example, `string` will return `false` if the underlying string container has a length of `0` and `true` otherwise.
That's why the `if` statement works.

When calling `encode` and `decode`, `errors=errors` is redundant and can be substituted by `errors`.
This assignment is used to call arguments in a different order but assigning them to the prototype's argument names.
This would be a correct way of writing those two lines:

```python
raw_bytes     = next_lang.encode(errors=errors, encoding=encoding)
cooked_string = raw_bytes.decode(errors=errors, encoding=encoding)
```
