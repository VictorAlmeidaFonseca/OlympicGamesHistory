from django.core.management.base import BaseCommand, CommandError
from django.db import Error
import csv
from olympic_api.models import TeamRegion



class Command(BaseCommand):
    help = "Populate the database with csv file."

    def team_to_csv(self):
        for_import = []
        with open('script/noc_regions.csv') as o:
            data = o.read()
            csv_team = csv.reader(data)
            team_csv = list(csv_team)
            for row in team_csv:
                to_import = TeamRegion()
                to_import.NOC = row[0]
                to_import.region = row[1]
                to_import.notes = row[2]
                for_import.append(to_import)
                for team in for_import:
                    TeamRegion.save()

    def handle(self, *args, **options):

        try:

            team_region_save = self.team_to_csv()
            team_region_save
            self.stdout.write(self.style.SUCCESS('Database was populated!'))


        except Error:
            raise CommandError('Exception is raised during the execution of a management command.')


