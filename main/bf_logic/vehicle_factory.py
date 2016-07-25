import random

from main.bf_logic.vehicle import Vehicle
from main.bf_logic.solder_factory import SolderFactory
from main.bf_logic.constants import NUM_OPERATORS_RANGE


class VehicleFactory:
    @classmethod
    def create(cls):
        vehicle = Vehicle()
        num_operators = random.choice(NUM_OPERATORS_RANGE)
        for i in range(num_operators):
            vehicle.add_operator((SolderFactory.create()))
        return vehicle