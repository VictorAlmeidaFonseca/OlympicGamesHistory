from .models import Athlete, TeamRegion, Champion
from rest_framework import serializers

class AthleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Athlete
        fields = "__all__"

class TeamRegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeamRegion
        fields = "__all__"


class ChampionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Champion
        fields = "__all__"