from main.bf_logic.solder import Solder


class SolderFactory:
    @classmethod
    def create(cls):
        solder = Solder()
        return solder
