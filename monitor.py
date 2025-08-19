
from time import sleep
import sys

def displayVitalsAlert(message):
  print(message)
  for i in range(6):
    print('\r* ', end='')
    sys.stdout.flush()
    sleep(1)
    print('\r *', end='')
    sys.stdout.flush()
    sleep(1)

def alert_not_in_range(message, value, min_value, max_value):
  if not is_in_range(value, min_value, max_value):
    displayVitalsAlert(message)
    return False
  return True

def is_in_range(value, min_value, max_value):
  return min_value <= value <= max_value

def isTemperatureOk(temperature):
  return alert_not_in_range('Temperature out of range', temperature, 95, 102)

def isPulseRateOk(pulseRate):
  return alert_not_in_range('Pulse Rate out of range!', pulseRate, 60, 100)

def isSpo2Ok(spo2):
  return alert_not_in_range('Oxygen Saturation out of range!', spo2, 90, 100)

def isBloodSugarOk(bloodSugar):
  return alert_not_in_range('Blood Sugar out of range!', bloodSugar, 70, 110)

def vitals_ok(temperature, pulseRate, spo2):
  return isTemperatureOk(temperature) and \
         isPulseRateOk(pulseRate) and isSpo2Ok(spo2)

def report_is_normal(values):
  vitals_map  = {
    'temperature': isTemperatureOk,
    'pulseRate': isPulseRateOk,
    'spo2': isSpo2Ok,
    'bloodSugar': isBloodSugarOk
  }
  for key, check in vitals_map.items():
    if not check(values[key]):
      return False
  return True