from django.apps import AppConfig


class MyProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_profile'

    def ready(self):
        import my_profile.signals