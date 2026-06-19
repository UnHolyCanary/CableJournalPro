from PySide6.QtGui import QStandardItemModel, QStandardItem


class LayersModel(QStandardItemModel):

    def __init__(self):
        super().__init__()

        self.setHorizontalHeaderLabels([
            "Слой",
            "Количество объектов"
        ])

    def update_data(self, layer_info):

        self.setRowCount(0)

        for layer, count in sorted(layer_info.items()):

            name_item = QStandardItem(layer)
            count_item = QStandardItem(str(count))

            self.appendRow([
                name_item,
                count_item
            ])