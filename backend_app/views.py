from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters import rest_framework
from .models import Akun, Pengguna, Jurnal, Konselor, Konseling
from .serializers import AkunSerializer, PenggunaSerializer, JurnalSerializer, KonselorSerializer, KonselingSerializer
from .filters import AkunFilter, PenggunaFilter, JurnalFilter, KonselorFilter, KonselingFilter

# Create your views here.


class AkunViewSet(viewsets.ModelViewSet):
    queryset = Akun.objects.all()
    serializer_class = AkunSerializer
    filterset_class = AkunFilter

    filter_backends = [filters.OrderingFilter,
                       rest_framework.DjangoFilterBackend]



class PenggunaViewSet(viewsets.ModelViewSet):
    queryset = Pengguna.objects.all()
    serializer_class = PenggunaSerializer
    filterset_class = PenggunaFilter

    filter_backends = [filters.OrderingFilter,
                       rest_framework.DjangoFilterBackend]


class JurnalViewSet(viewsets.ModelViewSet):
    queryset = Jurnal.objects.all()
    serializer_class = JurnalSerializer
    filterset_class = JurnalFilter

    filter_backends = [filters.OrderingFilter,
                       rest_framework.DjangoFilterBackend]


class KonselorViewSet(viewsets.ModelViewSet):
    queryset = Konselor.objects.all()
    serializer_class = KonselorSerializer
    filterset_class = KonselorFilter

    filter_backends = [filters.OrderingFilter,
                       rest_framework.DjangoFilterBackend]


class KonselingViewSet(viewsets.ModelViewSet):
    queryset = Konseling.objects.all()
    serializer_class = KonselingSerializer
    filterset_class = KonselingFilter

    filter_backends = [filters.OrderingFilter,
                       rest_framework.DjangoFilterBackend]


