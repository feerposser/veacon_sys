from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

pnconfig = PNConfiguration()

pnconfig.subscribe_key = 'sub-c-6d91b8ee-235e-11ea-894a-b6462cb07a90'
pnconfig.publish_key = 'pub-c-600c2815-a5c1-4410-9ac6-669023a7d73c'

pubnub = PubNub(pnconfig)


def my_publish_callback(envelope, status):
    # Check whether request successfully completed or not
    if not status.is_error():
        pass  # Message successfully published to specified channel.
    else:
        pass  # Handle message publish error. Check 'category' property to find out possible issue
        # because of which request did fail.
        # Request can be resent using: [status retry];


class MySubscribeCallback(SubscribeCallback):
    @staticmethod
    def send_message(message):
        pubnub.publish().channel("veacon").message(message).pn_async(my_publish_callback)
