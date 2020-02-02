from django.shortcuts import render
from rest_framework import viewsets
from .models import Athlete, TeamRegion, Game, Event, Sport, Champion
from .serializers import AthleteSerializer, TeamRegionSerializer, GameSerializer, EventSerializer, SportSerializer, \
                        ChampionSerializer

class AthleteViewSet(viewsets.ModelViewSet):
    """
    API endpoint allow Athletes to be viewed or edited.
    """
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer


class TeamRegionViewSet(viewsets.ModelViewSet):
    """
    API endpoint allow TeamRegion to be viewed or edited.
    """
    queryset = TeamRegion.objects.all()
    serializer_class = TeamRegionSerializer


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint allow TeamRegion to be viewed or edited.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint allow TeamRegion to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class SportViewSet(viewsets.ModelViewSet):
    """
    API endpoint allow TeamRegion to be viewed or edited.
    """
    queryset = Sport.objects.all()
    serializer_class = SportSerializer


class ChampionViewSet(viewsets.ModelViewSet):
    """
    API endpoint allow TeamRegion to be viewed or edited.
    """
    queryset = Champion.objects.all()
    serializer_class = ChampionSerializer



