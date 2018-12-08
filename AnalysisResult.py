from models.Disease import Disease
from models.Analysis import Analysis


class AnalysisResult:
    """An AnalysisResult object contains the result of an executed analysis.

    Attributes:
        id    Identification number of this object
        analysis    Analysis object that gave this result
        disease    Disease object that was predicted by the Analysis classifier
        score    Score of result certainty
        frame    peace of image that went submited to prediction
    """


    def __init__(self,
                 id=0,
                 analysis=Analysis(),
                 disease=Disease(),
                 score=0,
                 frame='0,0,0,0'):
        """AnalisysResult model constructor

        args:
            id: Integer ID number
            analysis: Analysis object that gave this result
            disease: Disease object that was predicted by the Analysis classifier
            score: Score of result certainty
            frame: peace of image that went submited to prediction
        """
        self.id = id
        self.analysis = analysis
        self.disease = disease
        self.score = score
        self.frame = frame
