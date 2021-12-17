import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import xml.etree.ElementTree as ET


class Inventory:
    def csv_reader(path):
        with open(path) as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')
            data = []
            for row in reader:
                data.append(row)

        return data
    
    def json_reader(path):
        with open(path) as file:
            return json.load(file)

    @classmethod
    def import_data(cls, path, report_type):
        dict_list = []
        file_type = path.split(".")[1]

        if file_type == 'csv':
            dict_list = cls.csv_reader(path)
        elif file_type == 'json':
            dict_list = cls.json_reader(path)

        if report_type == "simples":
            return SimpleReport.generate(dict_list)
        else:
            return CompleteReport.generate(dict_list)

        

print(Inventory.import_data('inventory_report/data/inventory.json', 'completo'))