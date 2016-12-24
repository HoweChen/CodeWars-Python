import math


class Fighter(object):

    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack


def declare_winner(fighter1, fighter2, first_attacker):
    # Code your solution here
    if first_attacker == fighter2.name:
        fighter1, fighter2 = fighter2, fighter1
    result = get_winner(fighter1, fighter2)
    return result.name


def get_winner(fighter1, fighter2):
    fighter1_win_round = math.ceil(
        fighter1.health / fighter2.damage_per_attack)
    fighter2_win_round = math.ceil(
        fighter2.health / fighter1.damage_per_attack)
    # mod_1 = fighter1_win_round % 1
    # mod_2 = fighter2_win_round % 1

    # if mod_1 != 0:
    #     fighter1_win_round = fighter1_win_round - mod_1 + 1
    # if mod_2 != 0:
    #     fighter2_win_round = fighter2_win_round - mod_2 + 1
    # print(fighter1_win_round)
    # print(fighter2_win_round)
    if fighter1_win_round >= fighter2_win_round:
        return fighter1
    else:
        return fighter2


fighter_1 = Fighter("Lew", 10, 2)
fighter_2 = Fighter("Harry", 5, 4)
print(declare_winner(fighter_1, fighter_2, 'Lew'))
print(declare_winner(fighter_1, fighter_2, 'Harry'))
print(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry"))
print(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Harald"))

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
