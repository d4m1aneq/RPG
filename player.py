class Player():
    def __init__(self, name, attack, health):
        self.health = health
        self.name = name
        self.attack = attack

    def __str__(self):
      return self.name.capitalize()

    def calculate_damage(self, damage_amount, attacker):
        self.health -= damage_amount
        print(f"The {attacker} attacks, {self} takes {damage_amount} damage")
        if self.health <= 0:
            print(f"{self.name.capitalize()} is dead.")
                   