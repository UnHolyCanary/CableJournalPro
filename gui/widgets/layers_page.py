from PySide6.QtWidgets import QHeaderView
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTableView,
    QLineEdit,
)

from gui.models.layers_model import LayersModel


class LayersPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        self.search = QLineEdit()
        self.search.setPlaceholderText("🔍 Поиск слоя...")

        layout.addWidget(self.search)

        self.table = QTableView()

        self.model = LayersModel()

        self.table.setModel(self.model)
        self.search.textChanged.connect(self.filter_layers)
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)

        self.table.setSelectionBehavior(QTableView.SelectRows)
        self.table.setSelectionMode(QTableView.SingleSelection)

        self.table.setSortingEnabled(True)
        self.table.setAlternatingRowColors(True)

        self.table.setSortingEnabled(True)

        self.table.setAlternatingRowColors(True)

        self.table.horizontalHeader().setStretchLastSection(True)

        layout.addWidget(self.table)

    def update_project(self, project):
        self.model.update_data(project.layer_info)

    def filter_layers(self, text):
        text = text.lower()

        for row in range(self.model.rowCount()):
            item = self.model.item(row, 0)
            if item is None:
                continue
            layer = item.text().lower()
            hidden = text not in layer
            self.table.setRowHidden(row, hidden)