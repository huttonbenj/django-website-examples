from django.apps import AppConfig


class AboutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'
    verbose_name = 'Pages'
    verbose_name_plural = 'Pages'
    def ready(self):
        import about.signals 