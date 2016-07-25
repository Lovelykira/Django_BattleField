import time
import random

from main.bf_logic.unit import Unit
from main.bf_logic.constants import START_SOLDER_EXPERIENCE, MAX_SOLDER_EXPERIENCE


class Solder(Unit):
    def __init__(self):
        super().__init__()
        self._experience = START_SOLDER_EXPERIENCE

    def do_attack(self):
        if self.can_attack():
            self._next_attack_in = self._recharge
            if self._experience != MAX_SOLDER_EXPERIENCE:
                self._experience += 1
            return self.get_power()
        else:
            self._next_attack_in -= 1
            return 0



    def take_damage(self, dmg):
        self._armor = self.calc_armor()
        if self._armor < dmg:
            self._health = self._health - dmg + self._armor

    def calc_armor(self):
        return 0.05 + self._experience / 100

    def get_experience(self):
        return self._experience

    def get_power(self):
        return 0.5 * (1 + self._health) * random.randint(50 + self._experience, 100) / 100
