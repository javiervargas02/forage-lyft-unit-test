from Battery.nubbin_battery import nubbin
from Battery.spindler_battery import spindler

from Engine.capulet_engine import capulet
from Engine.sternman_engine import sternman
from Engine.willoughby_engine import willoughby

from car import car

from datetime import date

class carFactory:
    @staticmethod
    def create_calliope(current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int) -> car:
        engine = capulet(current_mileage, last_service_mileage)
        battery = spindler(current_date, last_service_date)
        return car(engine, battery)

    @staticmethod
    def create_glissade(current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int) -> car:
        engine = willoughby(current_mileage, last_service_mileage)
        battery = spindler(current_date, last_service_date)
        return car(engine, battery)

    @staticmethod
    def create_palindrome(current_date : date, last_service_date : date, warning_light_is_on : bool) -> car:
        engine = sternman(warning_light_is_on)
        battery = spindler(current_date, last_service_date)
        return car(engine, battery)

    @staticmethod
    def create_rorschach(current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int) -> car:
        engine = willoughby(current_mileage, last_service_mileage)
        battery = nubbin(current_date, last_service_date)
        return car(engine, battery)

    @staticmethod
    def create_thovex(current_date : date, last_service_date : date, current_mileage : int, last_service_mileage : int) -> car:
        engine = capulet(current_mileage, last_service_mileage)
        battery = nubbin(current_date, last_service_date)
        return car(engine, battery)