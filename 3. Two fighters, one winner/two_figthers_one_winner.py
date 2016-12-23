class Fighter(object):

    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack


def declare_winner(fighter1, fighter2, first_attacker):
    # Code your solution here
    if first_attacker == fighter1.name:
        pass
    else:
        # change fighter order
        fighter1, fighter2 = fighter2, fighter1
    fight_round = 1
    # while fighter1.health>=0 or fighter2.health>=0:


fithter_1 = Fighter("Lew", 10, 2)
fithter_2 = Fighter("Harry", 5, 4)
# print(fithter_1.name)


# Create a function that returns the name of the winner in a fight between
# two fighters.

# Each fighter takes turns attacking the other and whoever kills the other
# first is victorious. Death is defined as having health <= 0.

# Each fighter will be a Fighter object/instance. See the Fighter class
# below in your chosen language.

# Both health and damagePerAttack (damage_per_attack for python) will be
# integers larger than 0. You can mutate the Fighter objects.

# Example:

# declareWinner(new Fighter("Lew", 10, 2), new Fighter("Harry", 5, 4),
# "Lew") => "Lew"

#   // Python
# declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew") =>
# "Lew"

#   Lew attacks Harry; Harry now has 3 health.
#   Harry attacks Lew; Lew now has 6 health.
#   Lew attacks Harry; Harry now has 1 health.
#   Harry attacks Lew; Lew now has 2 health.
#   Lew attacks Harry: Harry now has -1 health and is dead. Lew wins.
