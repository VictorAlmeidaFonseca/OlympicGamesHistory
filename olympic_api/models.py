from django.db import models


# Variable to store the choices providing sex types.
SexType =  models.TextChoices('Sex', 'M F')

# Variable to store the choices providing medal types.
MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE NA')

# Variable to store the choices providing season game types.
SeasonType = models.TextChoices('SeasonType', 'SUMMER WINTER')


class TeamRegion(models.Model):
    """
    Class for store information about teams who have been to the Olympic Games
    """
    name = models.CharField(max_length=500, null=False, blank=False, help_text="Field store the team's name")
    noc = models.CharField(max_length=3, null=False, blank=False, help_text="Field store the initials of National "
                                                                            "Olympic Committee")
    notes = models.CharField(max_length=255, null=True, blank=True)


class Athlete(models.Model):
    """
    Class for store information about athletes who have been to the Olympic Games.
    """
    name = models.CharField(max_length=500, null=False, blank=False, help_text="Field store the Athlete's name")
    sex = models.CharField(max_length=1, null=False, blank=False,  choices=SexType.choices, help_text="Field store the "
                                                                                              "Athlete's sex")
    age = models.IntegerField(null=False, blank=False)
    height = models.IntegerField(help_text="Field store the Athlete's height in centimeters")
    weight = models.IntegerField(help_text="Field store the Athlete's weight in kilograms")
    team_region = models.ForeignKey(TeamRegion, null=False, blank=False, on_delete=models.PROTECT, help_text="Field store foreing "
                                                                                                 "key refers to "
                                                                                                 "TeamRegion primary "
                                                                                                 "key")

class Game(models.Model):
    """
    Class for storing information about the  Olympic Games.
    """
    year = models.IntegerField(null=False, blank=False, help_text="Field store the year of the game")
    season =  models.CharField(max_length=6, choices=SeasonType.choices, null=False, blank=False, help_text="Field store the season of the game")
    city = models.CharField(max_length=30, null=False, blank=False, help_text="Field store the city of the game")


class Sport(models.Model):
    """
    Class for store information about the sports on the Olympic Games.
    """
    name = models.CharField(max_length=500, null=False, blank=False, help_text="Field store the Sport's name")


class Event(models.Model):
    """
    Class for store types of events on the Olympic Games.
    """
    sport = models.ForeignKey(Sport, null=False, blank=False, on_delete=models.PROTECT, help_text="Field store foreing "
                                                                                                 "key refers to "
                                                                                                 "primary key on the "
                                                                                                 "entity Sport")
    gender = models.CharField(max_length=1, null=False, blank=False,  choices=SexType.choices, help_text="Field store the "
                                                                                              "event's gender")
    description = models.CharField(max_length=500, null=False, blank=False, help_text="Field store the description of "
                                                                                      "the event")


class Champion(models.Model):
    """
    Class for store the champions of the Olympic Games.
    """
    athlete = models.ForeignKey(Athlete, null=False, blank=False, on_delete=models.PROTECT, help_text="Field store foreing"
                                                                                                 "key refers to primary "
                                                                                                 "key on the entity Athlete")
    event = models.ForeignKey(Event, null=False, blank=False, on_delete=models.PROTECT, help_text="Field store foreing"
                                                                                                 "key refers to primary "
                                                                                                 "key on the entity Event")
    medal = models.CharField(max_length=6, null=False, blank=False,  choices=MedalType.choices, help_text="Field store the "
                                                                                              "Athlete's medal")