from core.equipment_detector import EquipmentDetector
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem


class BlocksModel(QStandardItemModel):

    def __init__(self):
        super().__init__()

        self.setHorizontalHeaderLabels([
            "Имя блока", 
            "Количество",
            "Тип оборудования"
            ])

    def update_data(self, block_info):

        self.setRowCount(0)

        for block, count in sorted(block_info.items()):

            name = QStandardItem(str(block))
            qty = QStandardItem(str(count))
            equipment = QStandardItem(
                EquipmentDetector.detect(block)
                )
            self.appendRow(
                [name,
                 qty,
                 equipment
                 ])
