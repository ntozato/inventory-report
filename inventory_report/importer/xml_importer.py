from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET

class XmlImporter(Importer):
    def import_data(path):
        file_type = path.split('.')[1]

        if file_type != 'xml':
            raise ValueError('Arquivo inválido')

        dict_list = []
        document = ET.parse(path)
        root = document.getroot()
        for record in root:
            tag_dict = {}
            for line in record:
                tag_dict[line.tag] = line.text
            dict_list.append(tag_dict)
        return dict_list

print(XmlImporter.import_data('inventory_report/data/inventory.xml'))
