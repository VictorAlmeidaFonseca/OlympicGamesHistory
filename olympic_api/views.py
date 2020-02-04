from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets, generics
from .models import Athlete, TeamRegion, Champion
from .serializers import AthleteSerializer, TeamRegionSerializer, ChampionSerializer


class AthleteViewSet(viewsets.ModelViewSet):
    """
    API endpoint allow Athletes to be viewed or edited.
    The API can be filtered by name, age, team_region or noc using exactly the same value in the field. The fields in
    filter can be optional.

    """
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'age', 'noc_team_region__name', 'noc_team_region']


class TeamRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint allow Athlete's Team Region to be viewed or edited.
    The API can be filtered by name and/or noc using exactly the same value in the field. The fields in
    filter can be optional.
    """
    queryset = TeamRegion.objects.all()
    serializer_class = TeamRegionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'noc',]


class ChampionViewSet(viewsets.ModelViewSet):
    """
    API endpoint allow Events to be viewed or edited.
    The API can be filtered by athlete, event and/or medal using exactly the same value in the field. The fields in
    filter can be optional.
    """
    queryset = Champion.objects.all()
    serializer_class = ChampionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['game', 'city' , 'athlete' , 'event' , 'medal']
