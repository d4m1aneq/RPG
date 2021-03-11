from player import Player 

class TestSuite:
  def test_human_damage():
    test_human = Player('human', 15, 100)
    test_human.calculate_damage(20, 'computer')
    test_human.calculate_damage(25, 'computer')
    assert test_human.health == 55