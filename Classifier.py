from models.Plant import Plant




class Classifier:
    def __init__(self,
		     id=0, 
		     plant=Plant(), 
		     tag="", 
		     path="",
		     analyses=list()):

	    self.id = id
	    self.plant = plant
	    self.tag = tag
	    self.path = path
	    self.analyses = analyses
