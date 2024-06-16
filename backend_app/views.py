from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters import rest_framework
from .models import Akun, Pengguna, JurnalPagi, JurnalSore, Konselor, Konseling
from .serializers import AkunSerializer, PenggunaSerializer, JurnalPagiSerializer, JurnalSoreSerializer, KonselorSerializer, KonselingSerializer
from .filters import AkunFilter, PenggunaFilter, JurnalPagiFilter, JurnalSoreFilter, KonselorFilter, KonselingFilter

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


class JurnalPagiViewSet(viewsets.ModelViewSet):
    queryset = JurnalPagi.objects.all()
    serializer_class = JurnalPagiSerializer
    filterset_class = JurnalPagiFilter

    filter_backends = [filters.OrderingFilter,
                       rest_framework.DjangoFilterBackend]
    
class JurnalSoreViewSet(viewsets.ModelViewSet):
    queryset = JurnalSore.objects.all()
    serializer_class = JurnalSoreSerializer
    filterset_class = JurnalSoreFilter

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


