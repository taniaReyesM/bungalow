import csv

from django.core.management.base import BaseCommand
from houses.models import House
from houses.utils import transform_data


class Command(BaseCommand):
    help = 'Creating model objects according the file path specified'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, help="file path")

    def handle(self, *args, **options):
        count = 0
        file_path = options['path']
        try:
            with open(file_path, 'rt') as csv_file:
                reader = csv.reader(csv_file, delimiter=',')
                header = next(reader, None)
                for row in reader:
                    count += 1
                    object_dict = {
                        key: value
                        for key, value in zip(header, row)
                    }
                    object_dict = transform_data(object_dict)
                    House.objects.create(**object_dict)

            print(f'{count} houses added to DB.')
        except Exception as e:
            print(f'Error: {e}')
