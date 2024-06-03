from django.contrib import admin
from .models import Akun, Pengguna, Konselor, Konseling, Jurnal
# Register your models here.
admin.site.register([Akun, Pengguna, Konselor, Konseling, Jurnal])