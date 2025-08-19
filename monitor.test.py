import unittest
import unittest.mock as mock
from monitor import vitals_ok, alert_not_in_range, report_is_normal


class MonitorTest(unittest.TestCase):
    @mock.patch('monitor.displayVitalsAlert')
    def test_no_alert_when_in_range(self, mock_alert):
        self.assertTrue(alert_not_in_range("Normal", 98, 95, 102))
        mock_alert.assert_not_called()

    @mock.patch('monitor.displayVitalsAlert')
    def test_alert_when_not_in_range(self, mock_alert):
        self.assertFalse(alert_not_in_range("Temperature out of Range", 94, 95, 102))
        mock_alert.assert_called_once_with("Temperature out of Range")
    
    @mock.patch('monitor.displayVitalsAlert')
    def test_temperature_ok(self, mock_alert):
        self.assertTrue(vitals_ok(98, 75, 95))
        mock_alert.assert_not_called()

    @mock.patch('monitor.displayVitalsAlert')
    def test_pulse_rate_critical(self, mock_alert):
        self.assertFalse(vitals_ok(98, 40, 95))
        mock_alert.assert_called_once_with('Pulse Rate out of range!')

    @mock.patch('monitor.displayVitalsAlert')
    def test_spo2_critical(self, mock_alert):
        self.assertFalse(vitals_ok(98, 75, 85))
        mock_alert.assert_called_once_with('Oxygen Saturation out of range!')
    
    @mock.patch('monitor.displayVitalsAlert')
    def test_all_vitals_ok(self, mock_alert):
        self.assertTrue(vitals_ok(98, 75, 95))
        mock_alert.assert_not_called()

    def test_report_is_normal(self):
        self.assertTrue(report_is_normal({
            'temperature': 98,
            'pulseRate': 75,
            'spo2': 95,
            'bloodSugar': 90
        }))

if __name__ == '__main__':
  unittest.main()
