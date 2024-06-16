from django.contrib import admin
from .models import Akun, Pengguna, Konselor, Konseling, JurnalPagi, JurnalSore
# Register your models here.
admin.site.register(
    [Akun, Pengguna, Konselor, Konseling, JurnalPagi, JurnalSore])
