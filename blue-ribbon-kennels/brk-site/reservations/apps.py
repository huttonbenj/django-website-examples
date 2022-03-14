from django.apps import AppConfig

class ReservationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reservations'
    def ready(self):
        import django.core.management
        django.core.management.call_command('init_kennel_objs')
        import reservations.signals 
        from reservations import updater
        updater.start()