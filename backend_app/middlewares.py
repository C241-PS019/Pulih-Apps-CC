import firebase_admin
from firebase_admin import auth
from .models import Akun, Pengguna
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.utils import timezone


class FirebaseAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None

        auth_parts = auth_header.split()

        if len(auth_parts) != 2 or auth_parts[0].lower() != 'bearer':
            return None

        id_token = auth_parts[1]

        try:
            decoded_token = auth.verify_id_token(id_token)
            user_id = decoded_token['uid']
            user_record: auth.UserRecord = auth.get_user(user_id)

            akun, created = Akun.objects.get_or_create(
                user_uid=user_id,
                defaults={
                    'identifier': user_record.email,
                    'providers': ','.join(user_record.provider_data[0].provider_id for provider_data in user_record.provider_data),
                    'created': timezone.now(),
                    'signed_in': timezone.now(),
                }
            )

            if created:
                # Only create Pengguna if Akun is newly created
                Pengguna.objects.create(
                    akun=akun,
                    nama=user_record.display_name or '',
                    nim='',
                    universitas='',
                    telepon=user_record.phone_number or ''
                )

            return (akun, None)
        except Exception as e:
            raise AuthenticationFailed(f'Authentication failed: {str(e)}')

    def authenticate_header(self, request):
        return 'bearer'