import random
import time
import logging
from abc import ABC, abstractmethod
 
 
logger = logging.getLogger('plane application')
logger.setLevel(logging.DEBUG)
 
stream_formatter = logging.Formatter('%(message)s')
stream_logger = logging.StreamHandler()
stream_logger.setLevel(logging.INFO)
stream_logger.setFormatter(stream_formatter)
logger.addHandler(stream_logger)
 
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_logger = logging.FileHandler('plane.log')
file_logger.setLevel(logging.DEBUG)
file_logger.setFormatter(file_formatter)
logger.addHandler(file_logger)
 
 
 
 
 
class Event(ABC):
    pass
 
#   @abstractmethod
#   def a(self):
#     pass
 
class Turbulence(Event):
    def generate(self):
        return random.gauss(0, 2)
 
 
class Correction(Event):
    rate = 1
 
    def correct_interference(self, angle, interference):
        angle += interference
        correction_value = self._get_correction_value()
        angle += -1 * correction_value if angle > 0 else correction_value
        return angle
 
    def _get_correction_value(self):
        # Some bussiness logic
        return random.gauss(0, 1 * self.rate)
 
 
 
class Environment:
    turbulence = Turbulence()
    wind_power = 0
 
    def update(self):
        wind_power = self.turbulence.generate()
 
 
class Plane:
    correction = Correction()
    wings_angle = 0.0
    name = None
 
    def __init__ (self, name):
        self.name = name
 
    def correct_wings_angle(self, wind_power):
        interference = self._get_interference(wind_power)
        self.wings_angle = self.correction.correct_interference(self.wings_angle, interference)
 
    def _get_interference(self, wind_power):
        # Some bussiness logic
 
        interference = wind_power
 
        return interference
 
 
 
if __name__ == "__main__":
    logger.info("Start of programm, to end press standard SIGINT")
    logger.info("Plane is flying...")
 
    env = Environment()
    airplane = Plane("Airplane 275")
 
    try:
        while True:
            env.update()
            airplane.correct_wings_angle(env.wind_power)
            print(airplane.wings_angle)
            logger.debug("Angle: %s", airplane.wings_angle)
            time.sleep(0.1)
 
            if airplane.wings_angle > 180:
                logger.info("Upside down!")
                break
    except KeyboardInterrupt:
        logger.info("End of programm")