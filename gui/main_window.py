from gui.widgets.layers_page import LayersPage
from gui.widgets.overview_page import OverviewPage
from core.report import ProjectReport
import PySide6.QtWidgets
from PySide6.QtGui import QAction

from core.project import Project


class MainWindow(PySide6.QtWidgets.QMainWindow):

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
        from PySide6.QtWidgets import QTabWidget

        # Центральный виджет
        central = PySide6.QtWidgets.QWidget()
        self.setCentralWidget(central)

        layout = PySide6.QtWidgets.QHBoxLayout(central)

        # Левая панель
        self.tree = PySide6.QtWidgets.QTreeWidget()
        self.tree.setHeaderLabel("Навигация")
        self.tree.setMaximumWidth(260)

        PySide6.QtWidgets.QTreeWidgetItem(self.tree, ["📁 Проект"])
        PySide6.QtWidgets.QTreeWidgetItem(self.tree, ["📊 Анализ"])
        PySide6.QtWidgets.QTreeWidgetItem(self.tree, ["📹 Видеонаблюдение"])
        PySide6.QtWidgets.QTreeWidgetItem(self.tree, ["🚪 СКУД"])
        PySide6.QtWidgets.QTreeWidgetItem(self.tree, ["🔥 ОПС"])
        PySide6.QtWidgets.QTreeWidgetItem(self.tree, ["🌐 ЛВС"])
        PySide6.QtWidgets.QTreeWidgetItem(self.tree, ["📡 Оптика"])
        PySide6.QtWidgets.QTreeWidgetItem(self.tree, ["📋 Кабельный журнал"])
        PySide6.QtWidgets.QTreeWidgetItem(self.tree, ["📦 Спецификация"])
        PySide6.QtWidgets.QTreeWidgetItem(self.tree, ["⚙ Настройки"])

        # Правая часть
        self.tabs = QTabWidget()

        self.overview = OverviewPage()
        self.layers = LayersPage()
        self.tabs.addTab(self.overview, "Обзор")
        self.tabs.addTab(self.layers, "Слои")

        layout.addWidget(self.tree)
        layout.addWidget(self.tabs)

    def open_dxf(self):

        filename, _ = PySide6.QtWidgets.QFileDialog.getOpenFileName(
            self, "Выберите DXF", "", "DXF (*.dxf)"
        )

        if not filename:
            return

        try:
            self.project.open(filename)

            self.overview.update_project(self.project)
            self.layers.update_project(self.project)
            self.statusBar().showMessage("DXF успешно открыт")

        except Exception as e:

            print(e)
            self.statusBar().showMessage("Ошибка открытия DXF")
