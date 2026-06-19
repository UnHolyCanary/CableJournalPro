from core.block_analyzer import BlockAnalyzer
from core import layer_analyzer
from core.layer_analyzer import LayerAnalyzer
from core.dxf_analyzer import DXFAnalyzer
from pathlib import Path
import ezdxf


class Project:
    """
    Главный объект проекта.
    """

    def __init__(self):
        self.layer_info = {}
        self.block_info = {}
        self.filename = ""
        self.name = ""
        self.folder = ""
     
        self.doc = None

        self.version = ""

        self.layers = []
        self.entities = []
        self.analyzer = None
        self.blocks = 0
        self.entities = 0
        self.types = {}
    def open(self, filename):
        self.doc = ezdxf.readfile(filename)
        self.analyzer = DXFAnalyzer(self.doc)

        info = self.analyzer.get_info()
        self.blocks = info["blocks"]
        self.entities = info["entities"]
        self.types = info["types"]
        self.info = info
        self.version = info.get("version", self.doc.dxfversion)
        self.layers = self.analyzer.get_layers()
        layer_analyzer = LayerAnalyzer(self.doc)
        self.layer_info = layer_analyzer.analyze()
        
        block_analyzer = BlockAnalyzer(self.doc)
        self.block_info = block_analyzer.analyze()

        file = Path(filename)
        self.filename = filename
        self.name = file.name
        self.folder = str(file.parent)

        return True
