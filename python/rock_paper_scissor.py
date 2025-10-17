#! /usr/bin/env python


import argparse
import logging
import random
import sys
from enum import Enum

logger = logging.getLogger(__name__)


class Choice(Enum):
    ROCK = 1, "🪨"
    PAPER = 2, "📄"
    SCISSOR = 3, "✂️"

    def __new__(cls, value, emoji):
        member = object.__new__(cls)
        member._value_ = value
        member.emoji = emoji
        return member

    @classmethod
    def print_choices(cls):
        print(
            f"Make your choice:\n{cls.ROCK.emoji}: {cls.ROCK.value}\n"
            f"{cls.PAPER.emoji}: {cls.PAPER.value}\n"
            f"{cls.SCISSOR.emoji} : {cls.SCISSOR.value}"
        )


class RockPaperScissor:
    def __init__(self, points):
        self.max_points = points
        self.scores = {"human": 0, "computer": 0}

    def process_result(self, h_choice, c_choice):
        def add_point(winner):
            self.scores[winner] += 1
            if winner == "human":
                who = "You"
            else:
                who = "Computer"
            print(f"{who} won the round!")

        print(f"{Choice(h_choice).emoji} vs. {Choice(c_choice).emoji}")

        logger.debug("Evaluating result.")

        if h_choice == c_choice:
            print("Repeat!")

        elif h_choice == Choice.ROCK.value:
            if c_choice == Choice.SCISSOR.value:
                add_point("human")
            elif c_choice == Choice.PAPER.value:
                add_point("computer")

        elif h_choice == Choice.PAPER.value:
            if c_choice == Choice.SCISSOR.value:
                add_point("computer")
            elif c_choice == Choice.ROCK.value:
                add_point("human")

        elif h_choice == Choice.SCISSOR.value:
            if c_choice == Choice.ROCK.value:
                add_point("computer")
            elif c_choice == Choice.PAPER.value:
                add_point("human")

    def print_scores(self):
        print(f"You: {self.scores['human']}\nComputer: {self.scores['computer']}")

    def play_round(self):
        c_choice = random.choice(
            [
                Choice.ROCK.value,
                Choice.PAPER.value,
                Choice.SCISSOR.value,
                Choice.SCISSOR.value,
            ]
        )
        logger.debug("Computers choice: %s", c_choice)
        while True:
            Choice.print_choices()
            logger.debug("Fetching user input.")
            h_choice = input()
            if h_choice not in [
                str(Choice.ROCK.value),
                str(Choice.PAPER.value),
                str(Choice.SCISSOR.value),
            ]:
                logger.debug('Invalid choice "%s" given.', h_choice)
                print("Invalid choice!")
                print()
                continue
            h_choice = int(h_choice)
            logger.debug("Users choice: %s", h_choice)
            break
        print()

        self.process_result(h_choice, c_choice)

    def run(self):
        logger.debug("Starting game. %s points to win.", self.max_points)
        first = True
        while (
            self.scores["human"] < self.max_points
            and self.scores["computer"] < self.max_points
        ):
            if not first:
                logger.debug("Not the first run, so we display the scores.")
                self.print_scores()
                print()
            logger.debug("Start round.")
            self.play_round()
            print()
            first = False

        print("Final scores:\n")
        self.print_scores()
        who = "You"
        if self.scores["human"] > self.scores["computer"]:
            who = "Computer"

        print(f"{who} won the game!")


def parse_arguments(args):
    parser = argparse.ArgumentParser(
        description="Rock, Paper, Scissor",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "-p",
        "--points",
        metavar="INTEGER",
        help="How many points to win (default: %(default)s)",
        type=int,
    )
    parser.set_defaults(points=1)

    return parser.parse_args(args)


def main():
    args = parse_arguments(sys.argv[1:])
    logger.debug("Initializing rock paper scissor.")
    game = RockPaperScissor(args.points)
    logger.debug("Run the game from main().")
    game.run()


if __name__ == "__main__":
    main()
