from rest_framework import serializers
from .models import Akun, Pengguna, Konselor, Konseling, Jurnal

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


class JurnalSerializer(serializers.ModelSerializer):
    pengguna_id = serializers.PrimaryKeyRelatedField(
        source='pengguna', queryset=Pengguna.objects.all(), write_only=True)
    pengguna = PenggunaSerializer(read_only=True)

    class Meta:
        model = Jurnal
        fields = "__all__"


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
