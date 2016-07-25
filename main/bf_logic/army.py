from main.bf_logic.log_saver import LogSaver
from main.bf_logic.random_strategy import RandomStrategy


class Army:
    def __init__(self, strategy=RandomStrategy):
        self._squads = []
        self._strategy = strategy

    def get_alive_squads(self):
        alive_squads = []
        for squad in self._squads:
            if squad.is_alive():
                alive_squads.append(squad)
        return alive_squads

    def take_damage(self, squad, dmg):
        squad.take_damage(dmg)

    def attack(self, enemy):
        log = []
        log.append("Attacker's army has {} squad(s) left:".format(len(self.get_alive_squads())))
        for squad in self.get_alive_squads():
            log.extend(squad.to_log())
        log.append("Defender's army has {} squad(s) left:".format(len(enemy.get_alive_squads())))
        for squad in enemy.get_alive_squads():
            log.extend(squad.to_log())
        for squad in self._squads:
            if not squad.is_alive():
                continue
            log.append("CALCULATE SQUADS DAMAGE:")
            enemy_squad = self._strategy.chose_squad(enemy_army=enemy)
            dmg = squad.attack()
            if dmg == 0:
                log.append("Attacker is charging")
                continue
            log.append("Attacker's dmg = {}".format(dmg))
            enemy.take_damage(enemy_squad, dmg)
            if enemy_squad.is_alive():
                return_dmg = enemy_squad.attack()
                if return_dmg == 0:
                    log.append("Defender is charging")
                    continue
                log.append("Defender's dmg = {}".format(return_dmg))
                self.take_damage(squad, return_dmg)

                if not squad.is_alive():
                    log.append("ATTACKER'S SQUAD DIES!")
            elif not enemy_squad.is_alive():
                log.append("DEFENDER'S SQUAD DIES!")

        if len(self.get_alive_squads()) == 0:
            log.append("Defender wins")

        if len(enemy.get_alive_squads()) == 0:
            log.append("Attacker wins")
        return log


    def add_group(self, group):
        self._squads.append(group)

    def is_alive(self):
        if len(self.get_alive_squads()) > 0:
            return True
        else:
            return False

    def get_strategy(self):
        return self._strategy.__name__

    def to_log(self):
        log = []
        log.append("Army' squads: ")
        for squad in self._squads:
            log.extend(squad.to_log())
        return log

    def __str__(self):
        squads = self.get_alive_squads()
        squads = '\n'.join([str(squad) for squad in squads])
        return 'Army with {} units: \n{}'.format(len(self.get_alive_squads()), squads)
