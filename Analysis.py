from models.Classifier import Classifier
from models.Image import Image


class Analysis:
    """An Analysis object contains information about an executed image analysis.

    Attributes:
        id: Identification number of this object
        image: Image object that has been used for this Analysis
        classifier: Classifier object that has been used for this Analysis
        analysis_results: A list of AnalysisResult object with all results
    """


    def __init__(self,
                 id=0,
                 image=Image(),
                 classifier=Classifier(),
                 analysis_results=[]):
        """Analisys model constructor
        Args:
            id: Integer number to identification
            image: Image object that has been used for this Analysis
            classifier: Classifier object that has been used for this Analysis
            analysis_results: A list of AnalysisResult object with all results
        """
        self.id = id
        self.image = image
        self.classifier = classifier
        self.analysis_results = analysis_results
