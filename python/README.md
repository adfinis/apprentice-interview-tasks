# Python

Open the file [rock_paper_scissor.py](./rock_paper_scissor.py) with a text editor
(right-click, then open with editor).

In a terminal, navigate to the python folder (`cd`). Execute the python file
(`./rock_paper_scissor.py`) and play a round of rock, paper, scissors.

Familiarize yourself with the game and the script. What features are provided?

## First Task

A bug has found its way into the script. Can you find it? Can you fix the bug?

## Second Task

Statistically, which option gives you the best chance of winning? Can you modify the
script so that no single option has a higher chance of winning?

## Third Task

If `Ctrl+c` or `Ctrl+d` is entered while the program is running, a `KeyboardInterrupt`
or `EOFError` is thrown, respectively.

Can you handle these situations so that the string `Good bye!` is displayed instead of
these errors?

## Fourth Task

The script contains several debug logs, but they are not currently displayed.

Implement a command-line interface (CLI) toggle to output debug messages
(`-v` / `--verbose`).

## Fifth Task

Currently, as in the physical game of rock, paper, scissors, there is an equal
probability of a win, a loss, or a draw. Can you adjust the script to ensure a 50:50
probability of winning or losing, making a draw impossible?

## Helpful Resources

  * Information on [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
  * Information on [argparse](https://docs.python.org/3/library/argparse.html)
  * Information on the [logging module](https://docs.python.org/3/library/logging.html)
