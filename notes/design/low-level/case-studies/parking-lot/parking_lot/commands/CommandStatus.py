from commands.AbstractCommand import AbstractCommand


class CommandStatus(AbstractCommand):
    def execute(self):
        return self.parking_lot.get_status()