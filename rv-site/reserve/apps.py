from django.apps import AppConfig


class ReserveConfig(AppConfig):
    name = 'reserve'
    def ready(self):
        import reserve.signals