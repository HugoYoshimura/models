from models.Plant import Plant


class Classifier:
	def __init__(self,
		     id=0, 
		     idPlant=0, 
		     tag="", 
		     path=""):
		self.id = id
		self.idPlant = idPlant
		self.tag = tag
		self.path = path
