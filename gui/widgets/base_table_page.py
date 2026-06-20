from PySide6.QtCore import Qt, QSortFilterProxyModel
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QTableView,
    QHeaderView,
)


class BaseTablePage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # Строка поиска
        self.search = QLineEdit()
        self.search.setPlaceholderText("🔍 Поиск...")
        layout.addWidget(self.search)

        # Таблица
        self.table = QTableView()
        self.table.verticalHeader().setVisible(False)
        # Прокси-модель для поиска и сортировки
        self.proxy = QSortFilterProxyModel()
        self.proxy.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.proxy.setFilterKeyColumn(0)

        layout.addWidget(self.table)

    def set_model(self, model):

        self.model = model

        self.proxy.setSourceModel(model)

        self.table.setModel(self.proxy)

        self.table.setSortingEnabled(True)
        self.table.setAlternatingRowColors(True)

        self.table.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QTableView.SelectionMode.SingleSelection)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)

        self.search.textChanged.connect(
            self.proxy.setFilterFixedString
        )