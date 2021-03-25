from django.urls import path, include, re_path
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('api/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    #path('auth/', include('djoser.urls.jwt')),
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

