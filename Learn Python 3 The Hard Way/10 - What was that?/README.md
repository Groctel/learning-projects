# Exercise 10

**What was that?**

## Running this program

```sh
python3 ex10.py
```

## What I did

I created some strings using escape sequences and printed them.

## What I learnt

These are all the escape sequecences Python supports:

| **Sequence** | **Description**                                     |
| :----------: | --------------------------------------------------- |
| `\\`         | Literal backslash (`\`).                            |
| `\'`         | Literal single quote (`'`).                         |
| `\"`         | Literal double quote (`"`).                         |
| `\a`         | ASCII bell (`BEL`).                                 |
| `\b`         | ASCII backspace (`BS`).                             |
| `\f`         | ASCII formfeed (`FF`).                              |
| `\n`         | ASCII linefeed (`LF`).                              |
| `\N{char}`   | Unicode character named `char`.                     |
| `\r`         | Carriage return (`CR`).                             |
| `\t`         | Horizontal tab (`TAB`).                             |
| `\uxxxx`     | Character with 16-bit hexadecimal value `xxxx`.     |
| `\Uxxxxxxxx` | Character with 32-bit hexadecimal value `xxxxxxxx`. |
| `\v`         | ASCII vertical tab (`VT`).                          |
| `\000`       | Character with octal value `000`.                   |
| `\xhh`       | Character with hexadecimal value `hh`.              |

These sequences are also supported by `"""` strings, which can also be delimited by `'''`.
