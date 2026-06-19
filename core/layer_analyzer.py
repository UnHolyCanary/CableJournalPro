from collections import defaultdict


class LayerAnalyzer:

    def __init__(self, doc):
        self.doc = doc
        self.modelspace = doc.modelspace()

    def analyze(self):

        layers = defaultdict(int)

        for entity in self.modelspace:
            layer = entity.dxf.layer
            layers[layer] += 1

        return dict(sorted(layers.items()))