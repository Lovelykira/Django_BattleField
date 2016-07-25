import random

from main.bf_logic.army_factory import ArmyFactory
from main.bf_logic.constants import STRATEGIES
from main.bf_logic.log_saver import LogSaver


class Battlefield:
    def __init__(self, num_armies):
        LogSaver.clear()
        self._armies = []
        for i in range(num_armies):
            self._armies.append(ArmyFactory.create(random.choice(STRATEGIES)))

    def get_alive_armies_log(self):
        log = []
        log.append("There are {} alive armies:".format(len(self.get_alive_armies())))
        for army in self._armies:
            log.append("{} - {}".format(self._armies.index(army), army.get_strategy()))
            log.extend(army.to_log())
        return log

    def get_alive_armies(self):
        alive_armies = []
        for army in self._armies:
            if army.is_alive():
                alive_armies.append(army)
        return alive_armies

    def get_rnd_army(self, excluded=[]):
        return random.choice([army for army in self._armies if army not in excluded and army.is_alive()])

    def next_step(self):
        attacker = self.get_rnd_army()
        defender = self.get_rnd_army([attacker])
        log = []
        log.append("NEW BATTLE army # {} ATTACKS army # {}. It's strategy is {}".format(self._armies.index(attacker), self._armies.index(defender), attacker.get_strategy()))
        attack_log = attacker.attack(defender)
        log.extend(attack_log)
        #LogSaver.add("<p>&ensp;NEW BATTLE army # {} ATTACKS army # {}. It's strategy is {}</p>".format(i, self._armies.index(target_army), self._armies[i].get_strategy()))

        if len(self.get_alive_armies()) == 1:
            winner = self.get_alive_armies()[0]
            log.append("ARMY # {} WINS THE WAR. {} IS THE BEST".format(self._armies.index(winner), winner.get_strategy()))
                #LogSaver.add("<p>&ensp;ARMY # {} WINS THE WAR. {} IS THE BEST</p>".format(i, self._armies[i].get_strategy()))
        return log




