import Pyside6

class Table(Pyside6.QtWidgets.QTableWidget)
    def __init__(self, parent = None):
        super().__init__.(parent)

    def add_data(self, data):
        self.data = data
        
