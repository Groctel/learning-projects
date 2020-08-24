# Exercise 15

**Reading Files**

## Running this program

```sh
python3 ex15.py ex15_sample.txt
```

## What I did

I used the `open` and `read` functions to respectively open and read the contents of a regular file.
I got the file name from both `argv` and `stdin`.

## What I learnt

When reading files, `read` returns a string that contains the whole file, so it can be passed directly to `print`.
Open files are an object of their own (like `std::fstream` objects in C++), so the `read` function is called directly from them.
