# Exercise 1

## Prompt

The present `after` routine for the mushroom is misleading, because it says the mushroom has been picked every time it's taken (which will be odd if it's taken, dropped and taken again).
Correct this.

## What I did

I copied the code from the book, formatting it in my own style, and added a `planted` variable to `mushroom`, which defaults to `true`.
Now, when `Take` is called, it checks if `planted == true` and prints the corresponding message in each case, updating the variable if necessary.

## What I learnt

Inform games start with some constants for the game and should include the `Parser`, `VerbLib` and `Grammar`, the latter being included at the end.

Objects are ordered in a tree by declaring them with the `Object (->)*` syntax, so that the object with *n* `->` is at the *nth* level of the tree and its parent is the first object with *n-1* `->` going upwards.

Objects can hold variables and attributes.
Variables are local data the objects are defined `with` and can have values or be their own routines (it looks like data variables are zero-ary functions with one implicit return statement like in Haskell).
Attributes are flags that every object `has` and can be set or unset, the latter being the default.

When issuing actions, the `before` routine for that action is activated before any changes to the game state and the `after`, when the game state has changed.

Just like C's `main` function, an `Initialise` function is required and must contain the initial `location` of the player.
