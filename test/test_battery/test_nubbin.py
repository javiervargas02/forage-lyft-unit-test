import unittest
from datetime import date
from Battery.nubbin_battery import nubbin

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_date = date.fromisoformat("2020-03-14")
        current_date = date.fromisoformat("2023-12-04")
        battery = nubbin(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

    def test_needs_service_false(self):
        last_service_date = date.fromisoformat("2023-12-04")
        current_date = date.fromisoformat("2027-12-04")
        battery = nubbin(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
