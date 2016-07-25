class LogSaver():
    log = []

    @classmethod
    def add(self, part):
        self.log.append(part)

    @classmethod
    def get_log(self):
        return self.log

    @classmethod
    def clear(cls):
        cls.log = []
