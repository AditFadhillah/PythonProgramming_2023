from enum import Enum
import random

class Result(Enum):
    WIN = 0
    DRAW = 1
    LOSS = 2

class Action(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def increase_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0

    def play(self):
        action = input(f"What will be your action [rock / paper / scissors]? ").strip().lower()
        if action in ("rock", "paper", "scissors"):
            return Action[action.upper()]
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            return self.play()

    def __str__(self):
        return f"Player {self.name} has {self.score} points."

class Bot(Player):
    def __init__(self):
        super().__init__("Bot")

    def play(self):
        return random.choice(list(Action))

class RockPaperScissors:
    def __init__(self, player1, player2, goal):
        self.player1 = player1
        self.player2 = player2
        self.goal = goal

    def play_round(self):
        action1 = self.player1.play()
        action2 = self.player2.play()

        if action1 == action2:
            return Result.DRAW
        elif (
            (action1 == Action.ROCK and action2 == Action.SCISSORS) or
            (action1 == Action.PAPER and action2 == Action.ROCK) or
            (action1 == Action.SCISSORS and action2 == Action.PAPER)
        ):
            self.player1.increase_score()
            return Result.WIN
        else:
            self.player2.increase_score()
            return Result.LOSS

    def start(self):
        while True:
            result = self.play_round()
            if result == Result.WIN:
                print(f"{self.player1.name} won this round!")
            elif result == Result.LOSS:
                print(f"{self.player2.name} won this round!")
            else:
                print("The round was a draw!")

            print(self.player1)
            print(self.player2)

            if self.player1.score == self.goal:
                print(f"The game has ended! Player {self.player1.name} won!")
                break
            elif self.player2.score == self.goal:
                print(f"The game has ended! Player {self.player2.name} won!")
                break

            print()

    def reset(self):
        self.player1.reset_score()
        self.player2.reset_score()

if __name__ == "__main__":
    player_name = input("Enter your name: ")
    player1 = Player(player_name)
    player2 = Bot()
    game = RockPaperScissors(player1, player2, 5)

    game.start()
