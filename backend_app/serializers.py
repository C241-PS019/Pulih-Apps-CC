from rest_framework import serializers
from .models import Akun, Pengguna, Konselor, Konseling, JurnalPagi, JurnalSore

# Model Serializer


class AkunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Akun
        fields = "__all__"


class PenggunaSerializer(serializers.ModelSerializer):
    akun_id = serializers.PrimaryKeyRelatedField(
        source='akun', queryset=Akun.objects.all(), write_only=True)
    akun = AkunSerializer(read_only=True)

    class Meta:
        model = Pengguna
        fields = "__all__"


class JurnalPagiSerializer(serializers.ModelSerializer):
    pengguna_id = serializers.PrimaryKeyRelatedField(
        source='pengguna', queryset=Pengguna.objects.all(), write_only=True)
    pengguna = PenggunaSerializer(read_only=True)

    class Meta:
        model = JurnalPagi
        fields = ['id', 'pengguna_id', 'pengguna',
                  "tanggal", 'q1', 'q2', 'q3', 'q4']
        read_only_fields = ['tanggal']


class JurnalSoreSerializer(serializers.ModelSerializer):
    pengguna_id = serializers.PrimaryKeyRelatedField(
        source='pengguna', queryset=Pengguna.objects.all(), write_only=True)
    pengguna = PenggunaSerializer(read_only=True)

    class Meta:
        model = JurnalSore
        fields = ['id', 'pengguna_id', 'pengguna', "tanggal",
                  'q1', 'q2', 'q3', 'q4', 'q5']
        read_only_fields = ['tanggal']


class KonselorSerializer(serializers.ModelSerializer):
    akun_id = serializers.PrimaryKeyRelatedField(
        source='akun', queryset=Akun.objects.all(), write_only=True)
    akun = AkunSerializer(read_only=True)

    class Meta:
        model = Konselor
        fields = "__all__"


class KonselingSerializer(serializers.ModelSerializer):
    pengguna_id = serializers.PrimaryKeyRelatedField(
        source='pengguna', queryset=Pengguna.objects.all(), write_only=True)
    pengguna = PenggunaSerializer(read_only=True)
    konselor_id = serializers.PrimaryKeyRelatedField(
        source='konselor', queryset=Konselor.objects.all(), write_only=True)
    konselor = KonselorSerializer(read_only=True)

    class Meta:
        model = Konseling
        fields = "__all__"
