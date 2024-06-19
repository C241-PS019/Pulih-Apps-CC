
from django_filters import rest_framework as filters
from .models import Akun, Pengguna, JurnalPagi, JurnalSore, Konselor, Konseling


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
    akun_id = filters.CharFilter(field_name='akun__user_uid', lookup_expr='icontains')
    nama = filters.CharFilter(field_name='nama', lookup_expr='icontains')
    nama_panggilan = filters.CharFilter(
        field_name='nama_panggilan', lookup_expr='icontains')
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
        fields = ['akun', 'nama', 'nama_panggilan',
                  'nim', 'universitas', 'telepon']


class JurnalPagiFilter(filters.FilterSet):
    judul = filters.CharFilter(field_name='judul', lookup_expr='icontains')
    pengguna = filters.CharFilter(
        field_name='pengguna', lookup_expr='icontains')
    tanggal = filters.DateFromToRangeFilter(field_name='tanggal')

    class Meta:
        model = JurnalPagi
        fields = ['judul', 'pengguna', 'tanggal']


class JurnalSoreFilter(filters.FilterSet):
    judul = filters.CharFilter(field_name='judul', lookup_expr='icontains')
    pengguna = filters.CharFilter(
        field_name='pengguna', lookup_expr='icontains')
    tanggal = filters.DateFromToRangeFilter(field_name='tanggal')

    class Meta:
        model = JurnalSore
        fields = ['judul', 'pengguna', 'tanggal']


class KonselorFilter(filters.FilterSet):
    akun_id = filters.CharFilter(field_name='akun__user_uid', lookup_expr='icontains')
    nama = filters.CharFilter(field_name='nama', lookup_expr='icontains')
    nama_panggilan = filters.CharFilter(
        field_name='nama_panggilan', lookup_expr='icontains')
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
        fields = ['akun', 'nama', 'nama_panggilan', 'nim', 'mitra', 'telepon']


class KonselingFilter(filters.FilterSet):
    pengguna = filters.CharFilter(
        field_name='pengguna', lookup_expr='icontains')
    konselor = filters.CharFilter(
        field_name='konselor', lookup_expr='icontains')
    jenis = filters.CharFilter(
        field_name='jenis', lookup_expr='icontains')
    tempat = filters.CharFilter(
        field_name='tempat', lookup_expr='icontains')
    tanggal = filters.CharFilter(field_name='tanggal', lookup_expr='icontains')
    waktu = filters.CharFilter(field_name='waktu', lookup_expr='icontains')
    pesan = filters.CharFilter(
        field_name='pesan', lookup_expr='icontains')
    tanggal_gte = filters.DateFilter(field_name='tanggal', lookup_expr='gte')
    tanggal_lte = filters.DateFilter(field_name='tanggal', lookup_expr='lte')
    waktu_gte = filters.TimeFilter(field_name='waktu', lookup_expr='gte')
    waktu_lte = filters.TimeFilter(field_name='waktu', lookup_expr='lte')
    status = filters.ChoiceFilter(
        field_name='status', choices=Konseling.Status.choices)

    class Meta:
        model = Konseling
        fields = ['pengguna', 'konselor', 'jenis', 'tempat', 'tanggal', 'waktu', 'pesan', 'status']
