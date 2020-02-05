from django.db import models


# Variable to store the choices providing sex types.
SexType =  models.TextChoices('Sex', 'M F')

# Variable to store the choices providing medal types.
MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE NA')


class TeamRegion(models.Model):
    """
    Class for store information about teams who have been to the Olympic Games
    """
    noc = models.CharField(max_length=3, null=False, blank=False, unique=True,
                           help_text="Field store the initials of National Olympic Committee.")

    name = models.CharField(max_length=500, null=False, blank=False, help_text="Field store the team's name")
    notes = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "team_region"

    def __str__(self):
        return self.name



class Athlete(models.Model):
    """
    Class for store information about athletes who have been to the Olympic Games.
    """
    name = models.CharField(max_length=500, null=False, blank=False, help_text="Field store the Athlete's name")
    sex = models.CharField(max_length=1, null=False, blank=False,  choices=SexType.choices,
                           help_text="Field store the Athlete's sex")

    age = models.IntegerField(null=False, blank=False, help_text="Field store the Athlete's age")
    height = models.IntegerField(help_text="Field store the Athlete's height in centimeters")
    weight = models.IntegerField(help_text="Field store the Athlete's weight in kilograms")
    noc_team_region = models.ForeignKey(TeamRegion, null=False, blank=False, on_delete=models.PROTECT, to_field='noc',
                                    help_text="Field store foreign key refers to TeamRegion noc field")

    class Meta:
        db_table = "athlete"

    def __str__(self):
        return self.name


class Champion(models.Model):
    """
    Class for store the champions of the Olympic Games.
    """
    game = models.CharField(max_length=500, null=False, blank=False, help_text="Field store the description of the event")
    city = models.CharField(max_length=30, null=False, blank=False, help_text="Field store the city of the game")

    athlete = models.ForeignKey(Athlete, null=False, blank=False, on_delete=models.PROTECT,
                                help_text="Field store foreing key refers to primary key on the entity Athlete")

    event = models.CharField(max_length=500, null=False, blank=False,
                                   help_text="Field store the description of the event")

    medal = models.CharField(max_length=6, null=False, blank=False,  choices=MedalType.choices,
                             help_text="Field store the Athlete's medal")

    class Meta:
        db_table = "champion"