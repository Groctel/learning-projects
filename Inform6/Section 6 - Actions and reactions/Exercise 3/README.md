# Exercise 3

## Prompt

"The door-handle of my room... was different from all other door-handles in the world, inasmuch as it seemed to open of its own accord and without my having to turn it, so unconscious had its manipulation become..." (Marcel Proust).
Use silent-running actions to make an unconsciously manipulated door: if the player tries to pass through when it's closed, print "(first opening the door)" and do so.
(You need to know some of S13, the section on doors, to answer this.)

## What I did

I created a room with a simple door and gave it a direction.

## What I learnt

When the player issued the `go through` action on an `openable` object that isn't `open` nor `locked`, the library automatically calls `open` on the target and prints the action without needing the user's input.
