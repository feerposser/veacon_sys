from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pprint import pprint

pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-6d91b8ee-235e-11ea-894a-b6462cb07a90"
pnconfig.publish_key = "pub-c-600c2815-a5c1-4410-9ac6-669023a7d73c"
pnconfig.uuid = "veacon_sys_django_server"
channel = "veaconChannel"

pubnub = PubNub(pnconfig)


class MySubscribeCallback(SubscribeCallback):

    def status(self, pubnub, status):
        pass

    def presence(self, pubnub, presence):
        pprint(presence.__dict__)

    def message(self, pubnub, message):
        pprint(message.__dict__)


class PubSubManager:

    @staticmethod
    def my_publish_callback(envelope, status):
        print(envelope.__dict__, '\n\n', status.__dict__)
        if not status.is_error():
            print('deu certo a publicação')
            pass  # worked
        else:
            print('deu errado a publicação')
            pass  # error

    def publish_in_gateway_channel(self, id, eddy_namespace, operation, gateway_id, content=None):
        """
        Publica no canal de um gateway
        :param eddy_namespace: Beacon que está sendo mirado
        :param operation: Operação que deve ser feita
        :param gateway_id: Id do gateway que será usado para o canal
        :param content: Conteúdo adicional
        :return:
        """
        try:
            assert operation in ("add", "rm"), \
                "operation not equals to 'add' or 'rm'. '%s' instead" % operation

            message = {
                "id": id,
                "sender": pnconfig.uuid,
                "eddy_namespace": eddy_namespace,
                "operation": operation,
                "gateway_id": gateway_id
            }

            if content:
                message["content"] = content

            pubnub.publish()\
                .channel("veacon_channel_gateway_%s" % gateway_id)\
                .message(message)\
                .should_store(True) \
                .pn_async(self.my_publish_callback)
        except Exception as e:
            print(e)

#
# pubnub.add_listener(MySubscribeCallback())
# pubnub.subscribe().channels(channel).execute()
# print("Listening %s pubnub channel" % channel)
