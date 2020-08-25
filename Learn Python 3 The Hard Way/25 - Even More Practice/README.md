# Exercise 25

**Even More Practice**

## Running this program

First, start `python3`:

```sh
python3
```

Next, import the program:

```python
import ex25.py
```

Run the following commands in order:

```python
sentence = "All good things come to those who wait."
words = ex25.break_words(sentence)
words
sorted_words = ex25.sort_words(words)
sorted_words
ex25.print_first_word(words)
ex25.print_last_word(words)
words
ex25.print_first_word(sorted_words)
ex25.print_last_word(sorted_words)
sorted_words
sorted_words = ex25.sort_sentence(sentence)
sorted_words
ex25.print_first_and_last(sentence)
ex25.print_first_and_last_sorted(sentence)
```

## What I did

I defined some functions to operate with strings of characters and called them from the interpreter's CLI.

## What I learnt

Multi-line strings (also called *docstrings*) can be used to document the behaviour of a function if they're not attached to a `print` statement.
The `python3` interpreter offers a CLI that can help me test and debug my programs.
