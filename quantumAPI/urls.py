"""
URL configuration for quantumAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from walk_in.views import WalkInViewSet, VenueViewSet, ApplicationView
from users.views import ProfileView, UserView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'api/walkin', WalkInViewSet, basename="WalkIn")
router.register(r'api/venue', VenueViewSet, basename="Venue")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/token/refresh', TokenRefreshView.as_view(), name="token_refresh"),
    path('api/profile', ProfileView.as_view(), name="Profile"),
    path('api/register', UserView.as_view(), name="User"),
    path("api/walkin/application", ApplicationView.as_view(), name="Application"),
    re_path(r'^', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
