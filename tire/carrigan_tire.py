from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, wear):
        self.wear = wear

    def needs_service(self):
        if any(wear >= 0.9 for wear in self.wear):
            return True
        else:
            return False
