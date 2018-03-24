from models.Classifier import Classifier
from models.Image import Image



class Analysis:
    def __init__(self,
                 id=0,
                 image=object(),
		 classifier=object()):
        self.id = id
        self.image = image
	self.classifier = classifier
