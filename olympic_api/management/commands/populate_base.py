from django.core.management.base import BaseCommand, CommandError
from django.db import Error
from django.db.models import query
from olympic_api.models import TeamRegion
import pandas
import csv


class Command(BaseCommand):
    help = "Populate the database with csv file."

    def handle(self, *args, **options):

        try:
           # with open('script/noc_regions.csv', newline='') as o:
           #     reader = csv.DictReader(o)
           #     for row in reader:
           #         noc=row['NOC'],
           #         name=row['region'],
           #         notes=row['notes'],
           #
           #    TeamRegion.objects.bulk_create(
           #         TeamRegion(NOC='noc'),
           #         TeamRegion(region='name'),
           #         TeamRegion(notes='notes'),
           #         )

           #     self.stdout.write(self.style.SUCCESS('Database was populated!'))

            team_region_csv = pandas.read_csv('script/noc_regions.csv')
            team_region_inter = team_region_csv.interrow()
            #team_region_name_csv = pandas.read_csv('script/noc_regions.csv', usecols = ["region"])
            #team_region_notes_csv = pandas.read_csv('script/noc_regions.csv', usecols = ["notes"])

            #team_region = [

            #    TeamRegion(
            #        noc = team_region_csv.iterrows()["NOC"],
            #        name=team_region_csv.iterrows()["region"],
            #        notes=team_region_csv.iterrows()["notes"]
            #    )
            #]

            TeamRegion.objects.create(**dict(team_region_inter))
            self.stdout.write(self.style.SUCCESS('Database was populated!'))
            #team_add = TeamRegion.objects.bulk_create(team_region)

            #if team_add.save():
            #    self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
        except Error:
            raise CommandError('Exception is raised during the execution of a management command.')

