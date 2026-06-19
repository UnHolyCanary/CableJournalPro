from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
)


class OverviewPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.table = QTableWidget()

        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Параметр", "Значение"])
        self.table.verticalHeader().setVisible(False)

        layout.addWidget(self.table)

    def update_project(self, project):

        rows = [
            ("Имя файла", project.name),
            ("Папка", project.folder),
            ("DXF версия", project.version),
            ("Количество слоев", str(len(project.layers))),
            ("Количество блоков", str(project.blocks)),
            ("Количество объектов", str(project.entities)),
        ]

        self.table.setRowCount(len(rows))

        for row, (name, value) in enumerate(rows):

            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(value))

        self.table.resizeColumnsToContents()