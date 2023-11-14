import unittest
from Engine.willoughby_engine import willoughby

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = willoughby(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 59999
        last_service_mileage = 0
        engine = willoughby(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
