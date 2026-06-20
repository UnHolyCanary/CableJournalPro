from gui.widgets.base_table_page import BaseTablePage
from gui.models.layers_model import LayersModel


class LayersPage(BaseTablePage):

    def __init__(self):
        super().__init__()

        self.set_model(LayersModel())

    def update_project(self, project):
        self.model.update_data(project.layer_info)