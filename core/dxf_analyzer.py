from collections import Counter


class DXFAnalyzer:

    def __init__(self, doc):
        self.doc = doc
        self.modelspace = doc.modelspace()

    def get_info(self):

        entity_counter = Counter()

        for entity in self.modelspace:
            entity_counter[entity.dxftype()] += 1

        return {
            "version": self.doc.dxfversion,
            "layers": len(self.doc.layers),
            "blocks": len(self.doc.blocks),
            "entities": len(self.modelspace),
            "types": entity_counter,
        }

    def get_layers(self):

        return sorted(layer.dxf.name for layer in self.doc.layers)
