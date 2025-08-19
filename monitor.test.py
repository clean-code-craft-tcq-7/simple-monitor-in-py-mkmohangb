import unittest
from monitor import vitals_ok, alert_not_in_range


class MonitorTest(unittest.TestCase):
    def test_no_alert_when_in_range(self):
        self.assertTrue(alert_not_in_range("Normal", 98, 95, 102))

    def test_alert_when_not_in_range(self):
        self.assertFalse(alert_not_in_range("Temperature out of Range", 94, 95, 102))
    
    def test_temperature_ok(self):
        self.assertTrue(vitals_ok(98, 75, 95))
    
    def test_pulse_rate_critical(self):
        self.assertFalse(vitals_ok(98, 40, 95))

    def test_spo2_critical(self):
        self.assertFalse(vitals_ok(98, 75, 85))
    
    def test_all_vitals_ok(self):
        self.assertTrue(vitals_ok(98, 75, 95))

if __name__ == '__main__':
  unittest.main()
