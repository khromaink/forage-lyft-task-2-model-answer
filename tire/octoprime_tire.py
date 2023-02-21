from tire.tire import Tire


class OctoprimeTire(Tire):

    def __init__(self, wear):
        self.wear = wear

    def needs_service(self):
        if sum(self.wear) >= 3:
            return True
        else:
            return False
