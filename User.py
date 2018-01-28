from models.Type import Type

class User:
    def __init__(self,
                 id=0,
                 idType=0,
                 email="",
                 username="",
                 password="",
                 salt="",
                 dateInsertion="",
                 dateUpdate=""):

        self.id = id
        self.idType = idType
        self.email = email
        self.username = username
        self.password = password
        self.salt = salt
        self.dateInsertion = dateInsertion
        self.dateUpdate = dateUpdate
