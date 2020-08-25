# Learn Python 3 The Hard Way

**A very simple introduction to the terrifyingly beautiful world of computers and code**

This project gathers the code from [Zed A. Shaw's book](https://www.amazon.com/Learn-Python-Hard-Way-Introduction/dp/0134692888)'s exercises.

## Running programs with `python3`

All throught the book, programs are run by calling `python3.6`.
Since my computer is using `python3.8` and other computers may be using different versions of Python 3, it's safer to just call `python3`, which is a symlink to the latest version the machine has installed:

```sh
ls -l /usr/bin/python3
# lrwxrwxrwx 1 root root 9 Jul 27 10:42 /usr/bin/python3 -> python3.8
```
