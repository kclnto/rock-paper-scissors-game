# !/usr/bin/env python3
# This program plays a game of Rock, Paper, Scissors between two Players,
# and reports both Player's scores each round.
import random
import time
import os
import sys

moves = ['rock', 'paper', 'scissors']


class Player():
    # The Player class is the parent class for all of the Players in this game.
    def __init__(self):
        self.score = 0
        self.my_move = None
        self.their_move = None

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class CyclePlayer(Player):
    # Player that cycles through rock, paper, scissors.
    def move(self):
        if self.my_move is None:
            self.my_move = "rock"
            return ("rock")
        elif self.my_move == "rock":
            self.my_move = "paper"
            return("paper")
        elif self.my_move == "paper":
            self.my_move = "scissors"
            return("scissors")
        else:
            return("rock")


class HumanPlayer(Player):
    # Allows input from a human player.
    def move(self):
        self.my_move = input("Rock, paper, or scissors?\n").lower()
        while True:
            if "rock" in self.my_move:
                return("rock")
            elif "paper" in self.my_move:
                return("paper")
            elif "scissors" in self.my_move:
                return("scissors")
            else:
                print_pause("Sorry, the only options are rock, paper or "
                            "scissors.")
                self.my_move = input("\nRock, paper, or scissors?\n\n").lower()


class RandomPlayer(Player):
    # Player that chooses an option at random.
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    # Returns the opponent's last move.
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            return self.their_move


class RockPlayer(Player):
    # Player that always plays rock.
    def move(self):
        return('rock')


def beats(one, two):
    # If player 1 beats player 2, returns "True".
    Player1Wins = ((one == 'rock' and two == 'scissors') or
                   (one == 'scissors' and two == 'paper') or
                   (one == 'paper' and two == 'rock'))
    return Player1Wins


def print_pause(string):
    # Adds a slightly dramatic pause.
    sys.stdout.flush()
    print(string)
    time.sleep(1)


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def give_score(self):
        # Displays the score after each round.
        print(f"Player 1 score:{self.p1.score}"
              f"\tPlayer 2 score:{self.p2.score}")
        sys.stdout.flush()

    def play_round(self):
        # Plays a single round of a game.
        move1 = self.p1.move()
        move2 = self.p2.move()

        print_pause(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move1, move2)
        if beats(move1, move2) is True:
            self.p1.score += 1
            print_pause("Player 1 wins the round.")
        elif beats(move1, move2) is False:
            if move1 == move2:
                print_pause("Tie round.")
            else:
                self.p2.score += 1
                print_pause("Player 2 wins the round.")

    def play_game(self):
        # Plays a game of 3 rounds.
        os.system('clear')
        print_pause("\nTime to rock...\n")
        print_pause("paper, scissors! Best of 3 rounds.")
        for round in range(1, 4):
            print_pause(f"\nRound {round}:")
            self.play_round()
            game.give_score()

        print_pause(f"\nFinal score:\n\nPlayer 1: {self.p1.score}"
                    f"  Player 2: {self.p2.score}\n")
        if self.p1.score > self.p2.score:
            print_pause("Player 1 wins!")
        elif self.p1.score < self.p2.score:
            print_pause("Player2 wins!")
        else:
            print_pause("It was a tie game!")
        print_pause("\nGame over.")


if __name__ == '__main__':
    # Listing all non-human opponents so a random opponent can be paired.
    opponent = [RockPlayer(), CyclePlayer(), RandomPlayer(), ReflectPlayer()]
    game = Game(HumanPlayer(), random.choice(opponent))

    game.play_game()
