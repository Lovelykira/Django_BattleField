class BFControl:
    __battlefields = dict()
    __logs = dict()
    __ID = 0

    @classmethod
    def add_battlfield(cls, ID, battlefield):
        cls.__battlefields[ID] = battlefield
        cls.__logs[ID] = []

    @classmethod
    def get_battlfield(cls, ID):
        return cls.__battlefields[ID]

    @classmethod
    def get_ID(cls):
        cls.__ID += 1
        return cls.__ID

    @classmethod
    def add_log(cls, ID, log):
        cls.__logs[ID].extend(log)

    @classmethod
    def get_log(cls, ID):
        return cls.__logs[ID]