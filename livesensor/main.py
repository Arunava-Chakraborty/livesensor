# testing exceptions
from sensor.exception import SensorException , error_message_detail
import os
import sys
from sensor.logger import logging


def test_exception():
    try:
        a = 1/0
    except Exception as e:
        logging.info(error_message_detail(e,sys))
        raise SensorException(e ,sys)

if __name__ == "__main__":
    try:
        test_exception()
    except Exception as e:
        print(e)