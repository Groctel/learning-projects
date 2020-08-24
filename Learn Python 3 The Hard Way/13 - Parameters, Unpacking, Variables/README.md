# Exercise 13

**Parameters, Unpacking, Variables**

## Running this program

```sh
python3 ex13.py ARG1 ARG2 ARG3
```

From now on, compulsory arguments will be written in `ALL_CAPS` and separated by spaces.
Optional arguments will be enclosed in `[]`.

## What I did

I used the `argv` module to read arguments from the command line and created a program that read a static number of arguments (4 in this case).

## What I learnt

When running programs with arguments, these need to be assigned at some point and their number has to be known (I guess variable `argc` is possible, but I don't know how to do that yet).
This process is called *unpacking* and the first argument `argv[0]` is always processed as the program's basename.
Calling the program with more or less arguments than expected returns an exception.
