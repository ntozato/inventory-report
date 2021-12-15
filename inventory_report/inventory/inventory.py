import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def import_data(path, report_type):
        dict_list = []

        with open(path) as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')
            for row in reader:
                dict_list.append(row)

        if report_type == "simples":
            return SimpleReport.generate(dict_list)
        else:
            return CompleteReport.generate(dict_list)
