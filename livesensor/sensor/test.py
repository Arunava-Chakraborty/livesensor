from sensor.exception import SensorException

try:
    1/0
except Exception as e:
    raise SensorException(e, sys)
