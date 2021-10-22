import random
import uuid
import time


class IOTDevice:
    def __init__(self):
        self.deviceId = uuid.uuid4()

    @property
    def temperature(self):
        return random.randint(0, 100)

    @property
    def latitude(self):
        return random.uniform(0, 180)

    @property
    def longitude(self):
        return random.uniform(-90, 90)

    @property
    def time(self):
        return time.time()

    def get_state(self):
        return {
            "data": {
                "deviceId": str(self.deviceId),
                "temperature": self.temperature,
                "location": {
                    "latitude": self.latitude,
                    "longitude": self.longitude,
                },
                "time": self.time
            }
        }
