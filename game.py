import random

def fight(computer, human):
    round = 1
    game_in_progress = True
    while game_in_progress and round < 11: 
        print(f"Round: {round}")
               
        damage1 = random.randint(0, human.attack) 
        damage2 = random.randint(0, computer.attack)  
        computer.calculate_damage(damage1, human) # human attack
        if computer.health > 0:
            human.calculate_damage(damage2, computer)  # computer attack
            
        if computer.health <= 0 or human.health <= 0:
            game_in_progress = False
            break
        print(f"{human} have {human.health} hp remaining, and the {computer} has {computer.health} hp remaining.")
        if round == 10 and (human.health > 0 and computer.health > 0):
            print("DRAW!")
        print()
        round += 1
  
