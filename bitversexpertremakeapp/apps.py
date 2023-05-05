from django.apps import AppConfig


class BitversexpertremakeappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bitversexpertremakeapp'

    def ready(self):
    	import bitversexpertremakeapp.signals