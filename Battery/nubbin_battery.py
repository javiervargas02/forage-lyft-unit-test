from .battery import battery

from datetime import date
class nubbin(battery):
    def __init__(self, last_service_date : date, current_date : date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_date = self.last_service_date.year
        todays_date = self.current_date.year
        return todays_date - service_date >= 4