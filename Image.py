from models.Disease import Disease
from models.Type import Type


class Image:
    def __init__(self,
                 id=0,
                 disease=Disease(),
                 url="",
                 description="",
                 source="",
                 size=0):
        self.id = id
        self.disease = disease
        self.url = url
        self.description = description
        self.source = source
        self.size = size
