from abc import ABC, abstractmethod
import json

class Importer(ABC):

    @abstractmethod
    def import_data(self, path):
        raise NotImplementedError
