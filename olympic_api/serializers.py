from .models import Athlete, Game, TeamRegion, Event, Sport, Champion
from rest_framework import serializers

class AthleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Athlete
        fields = "__all__"


class TeamRegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeamRegion
        fields = "__all__"


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"


class SportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sport
        fields = "__all__"


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class ChampionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Champion
        fields = "__all__"