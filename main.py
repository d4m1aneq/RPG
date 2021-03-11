from game import fight
from player import Player
from tests import TestSuite

START_HEALTH = 30

value = input("Select 1 for game, 2 for tests:\n")
if value == "1":
    computer = Player('computer',15, START_HEALTH)
    human = Player('human', 15, START_HEALTH)
    fight(computer, human)
else:
    TestSuite.test_human_damage()