from django.urls import path, include
from accounts import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('patientFeed', views.PatientInfoViewSet)

urlpatterns = [
    path('', include(router.urls))
]