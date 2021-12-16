import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def import_data(path, report_type):
        dict_list = []

        with open(path) as file:
            if path.endswith('.csv'):
                reader = csv.DictReader(file, delimiter=",", quotechar='"')
            if path.endswith('.json'):
                reader = json.load(file)
            if path.endswith('.xml'):
                tree = ET.parse(file)
                reader = tree.getroot()
            for row in reader:
                is_xml = path.endswith('.xml') 
                if (is_xml):
                    xml_dict = {}
                    for key in row:
                        xml_dict[key.tag] = key.text
                    dict_list.append(xml_dict)
                else:
                    dict_list.append(row)


        if report_type == "simples":
            return SimpleReport.generate(dict_list)
        else:
            return CompleteReport.generate(dict_list)

# solução para leitura do xml retirada de: https://stackabuse.com/reading-and-writing-xml-files-in-python/