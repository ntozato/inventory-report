from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        file_type = path.split('.')[1]

        if file_type != 'csv':
            raise ValueError('Arquivo inválido')

        with open(path) as file:
            dict_list = []
            reader = csv.DictReader(file, delimiter=",", quotechar='"')
            for row in reader:
                dict_list.append(row)
            return dict_list


# print(CsvImporter.import_data('inventory_report/data/inventory.csv'))
