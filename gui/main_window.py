from core.report import ProjectReport
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QFileDialog,
    QTreeWidget,
    QTreeWidgetItem,
    QTextEdit,
    QHBoxLayout,
)
from PySide6.QtGui import QAction

from core.project import Project


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.project = Project()

        self.setWindowTitle("CableJournal Pro 0.1 Alpha")
        self.resize(1300, 800)

        self.create_menu()
        self.create_statusbar()
        self.create_ui()

    def create_menu(self):

        file_menu = self.menuBar().addMenu("Файл")

        open_action = QAction("Открыть DXF", self)
        open_action.triggered.connect(self.open_dxf)

        exit_action = QAction("Выход", self)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(open_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

    def create_statusbar(self):
        self.statusBar().showMessage("Готов")

    def create_ui(self):

        central = QWidget()
        self.setCentralWidget(central)

        layout = QHBoxLayout(central)

        self.tree = QTreeWidget()
        self.tree.setHeaderLabel("Навигация")

        QTreeWidgetItem(self.tree, ["📁 Проект"])
        QTreeWidgetItem(self.tree, ["📊 Анализ"])
        QTreeWidgetItem(self.tree, ["📹 Видеонаблюдение"])
        QTreeWidgetItem(self.tree, ["🚪 СКУД"])
        QTreeWidgetItem(self.tree, ["🔥 ОПС"])
        QTreeWidgetItem(self.tree, ["🌐 ЛВС"])
        QTreeWidgetItem(self.tree, ["📡 Оптика"])
        QTreeWidgetItem(self.tree, ["📋 Кабельный журнал"])
        QTreeWidgetItem(self.tree, ["📦 Спецификация"])
        QTreeWidgetItem(self.tree, ["⚙ Настройки"])

        self.tree.setMaximumWidth(260)

        self.info = QTextEdit()
        self.info.setReadOnly(True)

        self.info.setPlainText(
            "Добро пожаловать в CableJournal Pro\n\n"
            "Откройте DXF через меню Файл → Открыть DXF"
        )

        layout.addWidget(self.tree)
        layout.addWidget(self.info)

    def open_dxf(self):

        filename, _ = QFileDialog.getOpenFileName(
            self, "Выберите DXF", "", "DXF (*.dxf)"
        )

        if not filename:
            return

        try:
            self.project.open(filename)

            self.info.setPlainText(ProjectReport.create(self.project))

            self.statusBar().showMessage("DXF успешно открыт")

        except Exception as e:

            self.info.setPlainText(str(e))
            self.statusBar().showMessage("Ошибка открытия DXF")
