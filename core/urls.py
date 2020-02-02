"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.urls import include, path
from rest_framework import routers
from olympic_api import views

router = routers.DefaultRouter()
router.register(r'athlete', views.AthleteViewSet)
router.register(r'teamregion', views.TeamRegionViewSet)
router.register(r'game', views.GameViewSet)
router.register(r'event', views.EventViewSet)
router.register(r'sport', views.SportViewSet)
router.register(r'champion', views.ChampionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('olympic/', include('rest_framework.urls', namespace='rest_framework')),
]
