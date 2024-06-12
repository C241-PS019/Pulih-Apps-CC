
from django_filters import rest_framework as filters
from .models import Akun, Pengguna, Jurnal, Konselor, Konseling


class AkunFilter(filters.FilterSet):
    user_uid = filters.CharFilter(
        field_name='user_uid', lookup_expr='icontains')
    identifier = filters.CharFilter(
        field_name='identifier', lookup_expr='icontains')
    providers = filters.CharFilter(
        field_name='providers', lookup_expr='icontains')
    created = filters.CharFilter(field_name='created', lookup_expr='icontains')
    signed_in = filters.CharFilter(
        field_name='signed_in', lookup_expr='icontains')
    
    created_gte = filters.DateTimeFilter(
        field_name='created', lookup_expr='gte')
    created_lte = filters.DateTimeFilter(
        field_name='created', lookup_expr='lte')
    signed_in_gte = filters.DateTimeFilter(
        field_name='signed_in', lookup_expr='gte')
    signed_in_lte = filters.DateTimeFilter(
        field_name='signed_in', lookup_expr='lte')

    class Meta:
        model = Akun
        fields = ['user_uid', 'identifier',
                  'providers', 'created', 'signed_in']


class PenggunaFilter(filters.FilterSet):
    # akun = filters.CharFilter(field_name='akun', lookup_expr='icontains')
    akun_id = filters.CharFilter(field_name='akun__user_uid', lookup_expr='icontains')
    nama = filters.CharFilter(field_name='nama', lookup_expr='icontains')
    nim = filters.CharFilter(field_name='nim', lookup_expr='icontains')
    universitas = filters.CharFilter(
        field_name='universitas', lookup_expr='icontains')
    telepon = filters.CharFilter(field_name='telepon', lookup_expr='icontains')
    
    created_gte = filters.DateTimeFilter(
        field_name='akun__created', lookup_expr='gte')
    created_lte = filters.DateTimeFilter(
        field_name='akun__created', lookup_expr='lte')
    signed_in_gte = filters.DateTimeFilter(
        field_name='akun__signed_in', lookup_expr='gte')
    signed_in_lte = filters.DateTimeFilter(
        field_name='akun__signed_in', lookup_expr='lte')

    class Meta:
        model = Pengguna
        fields = ['akun', 'nama', 'nim', 'universitas', 'telepon']


class JurnalFilter(filters.FilterSet):
    pengguna = filters.CharFilter(
        field_name='pengguna', lookup_expr='icontains')

    class Meta:
        model = Jurnal
        fields = ['pengguna']


class KonselorFilter(filters.FilterSet):
    akun = filters.CharFilter(field_name='akun', lookup_expr='icontains')
    nama = filters.CharFilter(field_name='nama', lookup_expr='icontains')
    nim = filters.CharFilter(field_name='nim', lookup_expr='icontains')
    mitra = filters.CharFilter(field_name='mitra', lookup_expr='icontains')
    telepon = filters.CharFilter(field_name='telepon', lookup_expr='icontains')
    
    created_gte = filters.DateTimeFilter(
        field_name='akun__created', lookup_expr='gte')
    created_lte = filters.DateTimeFilter(
        field_name='akun__created', lookup_expr='lte')
    signed_in_gte = filters.DateTimeFilter(
        field_name='akun__signed_in', lookup_expr='gte')
    signed_in_lte = filters.DateTimeFilter(
        field_name='akun__signed_in', lookup_expr='lte')

    class Meta:
        model = Konselor
        fields = ['akun', 'nama', 'nim', 'mitra', 'telepon']


class KonselingFilter(filters.FilterSet):
    pengguna = filters.CharFilter(
        field_name='pengguna', lookup_expr='icontains')
    konselor = filters.CharFilter(
        field_name='konselor', lookup_expr='icontains')
    waktu = filters.CharFilter(field_name='waktu', lookup_expr='icontains')
    persetujuan = filters.CharFilter(
        field_name='persetujuan', lookup_expr='icontains')
    pertemuan = filters.CharFilter(
        field_name='pertemuan', lookup_expr='icontains')
    
    waktu_gte = filters.DateTimeFilter(field_name='waktu', lookup_expr='gte')
    waktu_lte = filters.DateTimeFilter(field_name='waktu', lookup_expr='lte')
    pertemuan_gte = filters.DateTimeFilter(field_name='pertemuan', lookup_expr='gte')
    pertemuan_lte = filters.DateTimeFilter(field_name='pertemuan', lookup_expr='lte')

    class Meta:
        model = Konseling
        fields = ['pengguna', 'konselor', 'waktu', 'persetujuan', 'pertemuan']
