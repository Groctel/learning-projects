# Exercise 2

## Prompt

Except of course that now 'Ruins' won't compile, because Inform expects to find a room called `Square_Chamber` which the steps lead to.
Design one.

## What I did

I copied the `steps` object and added the `Square_Chamber`.

## What I learnt

Among others, these four attributes can be set for objects:

| **Attribute** | **Description**                                                                   |
| :-----------: | --------------------------------------------------------------------------------- |
| `door`        | The object works like a door which can be open and closed.                        |
| `open`        | The object is initially open.                                                     |
| `scenery`     | The object is part of the scenery, so it's not printed in the room's object list. |
| `static`      | The object cannot be picked by the player.                                        |

Doors can point to a `door_to` location, where they lead, and can be an exit to a `door_dir` direction.
In this case, the direction is `d_to` (down), so the door object was also specified as the `d_to` in `Forest` and it was reciprocated with `Stone_Chamber`'s `u_to`.
