# Exercise 16

**Reading and Writing Files**

## Running this program

```sh
python3 ex16.py FILENAME
```

## What I did

I used the `truncate` and `write` function to respectively remove the contents of a file and add new contents to it.

## What I learnt

When opening files, the file opening mode defaults to *read* (`r`), but other mode can be selected (copied verbatim from `pydoc open`):

| **Mode** | **Description**                                                  |
| :------: | ---------------------------------------------------------------- |
| `'r'`    | Open for reading (default).                                      |
| `'w'`    | Open for writing, truncating the file first.                     |
| `'x'`    | Create a new file and open it for writing.                       |
| `'a'`    | Open for writing, appending to the end of the file if it exists. |
| `'b'`    | Binary mode.                                                     |
| `'t'`    | Text mode (default).                                             |
| `'+'`    | Open a disk file for updating (reading and writing).             |
| `'U'`    | Universal newline mode (deprecated).                             |


Without using conditionals, `^C` can be issed to a program to terminate it with an interrupt (`SIGINT`).
I also edited the `write` statement for `line2` to print the linefeed using a formatted string, which look wicked.
