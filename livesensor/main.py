# testing exceptions
from sensor.exception import SensorException , error_message_detail
import os
import sys
from sensor.logger import logging
from sensor.utils import dump_data

'''''
def test_exception():
    try:
        a = 1/0
    except Exception as e:
        logging.info(error_message_detail(e,sys))
        raise SensorException(e ,sys)
'''
if __name__ == "__main__":
    file_path = "D:/livesensor/livesensor/aps_failure_training_set1.csv"
    database_name = "APS_Failure_Dataset"
    collection_name = "sensor_data"
    dump_data(file_path , database_name , collection_name)
    