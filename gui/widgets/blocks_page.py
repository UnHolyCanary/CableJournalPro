from gui.widgets.base_table_page import BaseTablePage
from gui.models.blocks_model import BlocksModel


class BlocksPage(BaseTablePage):

    def __init__(self):
        super().__init__()

        self.set_model(BlocksModel())

        self.search.setPlaceholderText("🔍 Поиск блока...")

    def update_project(self, project):

        self.model.update_data(project.block_info)