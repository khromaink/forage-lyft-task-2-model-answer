from abc import ABC


class Tire(ABC):
    class Tire:
        def __init__(self, wear):
            self.wear = wear

        def needs_service(self):
            raise NotImplementedError
