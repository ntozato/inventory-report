import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import xml.etree.ElementTree as ET


class Inventory:
    @classmethod
    def process_csv(cls, file):
        dict_list = []
        reader = csv.DictReader(file, delimiter=",", quotechar='"')
        for row in reader:
            dict_list.append(row)
        return dict_list

    @classmethod
    def process_json(cls, file):
        dict_list = []
        reader = json.load(file)
        for row in reader:
            dict_list.append(row)
        return dict_list

    @classmethod
    def process_xml(cls, file):
        dict_list = []
        document = ET.parse(file)
        root = document.getroot()
        for record in root:
            tag_dict = {}
            for line in record:
                tag_dict[line.tag] = line.text
            dict_list.append(tag_dict)
        return dict_list

    def import_data(path, report_type):
        with open(path) as file:
            dict_list = None
            if path.endswith('.csv'):
                dict_list = Inventory.process_csv(file)
            if path.endswith('.json'):
                dict_list = Inventory.process_json(file)
            if path.endswith('.xml'):
                dict_list = Inventory.process_xml(file)

        if report_type == "simples":
            return SimpleReport.generate(dict_list)
        else:
            return CompleteReport.generate(dict_list)

# solução para leitura do xml retirada de:
# https://stackabuse.com/reading-and-writing-xml-files-in-python/
