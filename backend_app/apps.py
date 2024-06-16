from django.apps import AppConfig
import firebase_admin
from firebase_admin import credentials
from django.conf import settings
import os


class BackendAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend_app'

    def ready(self):
        if not firebase_admin._apps:
            cred_path = os.path.join(
                settings.BASE_DIR, 'serviceAccountKey.json')
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred, {
                'storageBucket': 'capstone-lite.appspot.com'
            })
