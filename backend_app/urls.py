from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AkunViewSet, PenggunaViewSet, JurnalViewSet, KonselingViewSet, KonselorViewSet

router = DefaultRouter()
router.register(r'akuns', AkunViewSet)
router.register(r'penggunas', PenggunaViewSet)
router.register(r'jurnals', JurnalViewSet)
router.register(r'konselors', KonselorViewSet)
router.register(r'konseling', KonselingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]