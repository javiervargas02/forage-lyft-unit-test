from .engine import engine

class capulet(engine):
    def __init__(self, last_service_mileage : int, current_mileage : int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        service_mileage = self.last_service_mileage
        current_mileage = self.current_mileage
        return current_mileage - service_mileage >= 30000