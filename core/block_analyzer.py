from collections import defaultdict


class BlockAnalyzer:

    def __init__(self, doc):
        self.doc = doc
        self.modelspace = doc.modelspace()

    def analyze(self):

        blocks = defaultdict(int)

        for entity in self.modelspace:

            if entity.dxftype() != "INSERT":
                continue

            name = entity.dxf.name
            blocks[name] += 1

        return dict(sorted(blocks.items()))