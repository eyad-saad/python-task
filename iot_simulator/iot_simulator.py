import json
import pickle
import threading
from time import sleep

from iot_device import IOTDevice
from google.cloud import pubsub_v1
from google.api_core.exceptions import AlreadyExists

import os


project_id = "scenic-style-324209"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "scenic-style-324209-4e7f64c6cfe1.json"
os.environ["PUBSUB_PROJECT_ID"] = project_id
os.environ["PUBSUB_EMULATOR_HOST"] = "localhost:8085"


publisher_client = pubsub_v1.PublisherClient()
topic_path = publisher_client.topic_path(project_id, "test")
try:
    publisher_client.create_topic(request={"name": topic_path})
except AlreadyExists:
    pass

subscriber_client = pubsub_v1.SubscriberClient()
subscription_path = subscriber_client.subscription_path(
    project_id, "test"
)

try:
    subscriber_client.create_subscription(
        request={"name": subscription_path, "topic": topic_path, "push_config":{
          'push_endpoint': 'http://127.0.0.1:8000/events'
        }}

    )
except AlreadyExists:
    pass


class IOTSimulator:
    def __init__(self, n_devices: int = 3):
        self.n_devices = n_devices
        self.running = True

    def start(self):
        for device_index in range(self.n_devices):
            iot_device = IOTDevice()
            thread = threading.Thread(target=self.run_simulation, args=(iot_device,))
            thread.start()
        try:
            while True:
                sleep(1)
        except KeyboardInterrupt:
            self.running = False

    def run_simulation(self, iot_device: IOTDevice):
        while self.running:
            data = iot_device.get_state()
            publisher_client.publish(
                topic_path,
                data=pickle.dumps(data)
            )
            sleep(1)


iot_simulator = IOTSimulator()
iot_simulator.start()
