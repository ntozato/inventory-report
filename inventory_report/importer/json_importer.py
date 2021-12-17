from inventory_report.importer.importer import Importer
import json

class JsonImporter(Importer):
    def import_data(path):
        file_type = path.split('.')[1]

        if file_type != 'json':
            raise ValueError('Arquivo inválido')

        with open(path) as file:
            return json.load(file)

print(JsonImporter.import_data('inventory_report/data/inventory.json'))