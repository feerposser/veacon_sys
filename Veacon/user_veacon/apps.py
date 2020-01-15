from django.apps import AppConfig


class UserVeaconConfig(AppConfig):
    name = 'user_veacon'

    def ready(self):
        import user_veacon.signals
