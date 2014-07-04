bowling
=======

Problem Description
-------------------

Create a program, which, given a valid sequence of rolls for one line of
American Ten-Pin Bowling, produces the total score for the game.  Here are
some things that the program does not necessarily need to do:

  * check for valid rolls

  * check for correct number of rolls and frames

  * provide scores for intermediate frames


We can briefly summarize the scoring for this form of bowling:

  * Each game, or “line” of bowling, includes ten turns, or “frames” for the
    bowler.

  * In each frame, the bowler gets up to two tries to knock down all the pins.

  * If in two tries, he fails to knock them all down, his score for that frame
    is the total number of pins knocked down in his two tries.

  * If in two tries he knocks them all down, this is called a “spare” and his
    score for the frame is ten plus the number of pins knocked down on his
    next throw (in his next turn).

  * If on his first try in the frame he knocks down all the pins, this is
    called a “strike”.  His turn is over, and his score for the frame is ten
    plus the simple total of the pins knocked down in his next two rolls.

  * If he gets a spare or strike in the last (tenth) frame, the bowler gets to
    throw one or two more bonus balls, respectively.  These bonus throws are
    taken as part of the same turn.  If the bonus throws knock down all the
    pins, the process does not repeat: the bonus throws are only used to
    calculate the score of the final frame.

  * The game score is the total of all frame scores.


Examples
--------

  * 20 rolls, all misses:

        +---+---+  +---+---+  +---+---+  +---+---+  +---+---+
        | - | - |  | - | - |  | - | - |  | - | - |  | - | - |
        +---+---+  +---+---+  +---+---+  +---+---+  +---+---+
        |   0   |  |   0   |  |   0   |  |   0   |  |   0   |
        +-------+  +-------+  +-------+  +-------+  +-------+

        +---+---+  +---+---+  +---+---+  +---+---+  +---+---+---+
        | - | - |  | - | - |  | - | - |  | - | - |  | - | - |   |
        +---+---+  +---+---+  +---+---+  +---+---+  +---+---+---+
        |   0   |  |   0   |  |   0   |  |   0   |  |     0     |
        +-------+  +-------+  +-------+  +-------+  +-----------+

    Input: `--------------------`
    Score: 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 0

  * 20 rolls, 10 pairs of 9-and-miss:

        +---+---+  +---+---+  +---+---+  +---+---+  +---+---+
        | 9 | - |  | 9 | - |  | 9 | - |  | 9 | - |  | 9 | - |
        +---+---+  +---+---+  +---+---+  +---+---+  +---+---+
        |   9   |  |   9   |  |   9   |  |   9   |  |   9   |
        +-------+  +-------+  +-------+  +-------+  +-------+

        +---+---+  +---+---+  +---+---+  +---+---+  +---+---+---+
        | 9 | - |  | 9 | - |  | 9 | - |  | 9 | - |  | 9 | - |   |
        +---+---+  +---+---+  +---+---+  +---+---+  +---+---+---+
        |   9   |  |   9   |  |   9   |  |   9   |  |     9     |
        +-------+  +-------+  +-------+  +-------+  +-----------+

    Input: `9-9-9-9-9-9-9-9-9-9-`
    Score: 9 + 9 + 9 + 9 + 9 + 9 + 9 + 9 + 9 + 9 = 90

  * 21 rolls, 10 pairs of 5-and-spare, with a final 5:

        +---+---+  +---+---+  +---+---+  +---+---+  +---+---+
        | 5 | / |  | 5 | / |  | 5 | / |  | 5 | / |  | 5 | / |
        +---+---+  +---+---+  +---+---+  +---+---+  +---+---+
        |  15   |  |  15   |  |  15   |  |  15   |  |  15   |
        +-------+  +-------+  +-------+  +-------+  +-------+

        +---+---+  +---+---+  +---+---+  +---+---+  +---+---+---+
        | 5 | / |  | 5 | / |  | 5 | / |  | 5 | / |  | 5 | / | 5 |
        +---+---+  +---+---+  +---+---+  +---+---+  +---+---+---+
        |  15   |  |  15   |  |  15   |  |  15   |  |    15     |
        +-------+  +-------+  +-------+  +-------+  +-----------+

    Input: `5/5/5/5/5/5/5/5/5/5/5`
    Score: 15 + 15 + 15 + 15 + 15 + 15 + 15 + 15 + 15 + 15 = 150

  * 12 rolls, all strikes (“perfect game”):

        +---+---+  +---+---+  +---+---+  +---+---+  +---+---+
        | X |   |  | X |   |  | X |   |  | X |   |  | X |   |
        +---+---+  +---+---+  +---+---+  +---+---+  +---+---+
        |  30   |  |  30   |  |  30   |  |  30   |  |  30   |
        +-------+  +-------+  +-------+  +-------+  +-------+

        +---+---+  +---+---+  +---+---+  +---+---+  +---+---+---+
        | X |   |  | X |   |  | X |   |  | X |   |  | X | X | X |
        +---+---+  +---+---+  +---+---+  +---+---+  +---+---+---+
        |  30   |  |  30   |  |  30   |  |  30   |  |    30     |
        +-------+  +-------+  +-------+  +-------+  +-----------+

    Input: `XXXXXXXXXXXX`
    Score: 30 + 30 + 30 + 30 + 30 + 30 + 30 + 30 + 30 + 30 = 300

  * 17 rolls:

        +---+---+  +---+---+  +---+---+  +---+---+  +---+---+
        | X |   |  | 7 | / |  | 7 | 2 |  | 9 | / |  | X |   |
        +---+---+  +---+---+  +---+---+  +---+---+  +---+---+
        |  20   |  |  17   |  |   9   |  |  20   |  |  30   |
        +-------+  +-------+  +-------+  +-------+  +-------+

        +---+---+  +---+---+  +---+---+  +---+---+  +---+---+---+
        | X |   |  | X |   |  | 2 | 3 |  | 6 | / |  | 7 | / | 3 |
        +---+---+  +---+---+  +---+---+  +---+---+  +---+---+---+
        |  22   |  |  15   |  |   5   |  |  17   |  |    13     |
        +-------+  +-------+  +-------+  +-------+  +-----------+

    Input: `X7/729/XXX236/7/3`
    Score: 20 + 17 + 9 + 20 + 30 + 22 + 15 + 5 + 17 + 13 = 168
