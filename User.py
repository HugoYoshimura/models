class User:
    """
    User model used like a transfer object

    Attributes:
        id: User identifier
        idType: User type
        email: Email
        username: Username
        password: Password
        salt: password salt
        dateInsertion: When user was inserted
        dateUpdate: Last user update
        analysis: A list of analysis performed by user
    """
    def __init__(
            self,
            id=0,
            idType=0,
            email="",
            username="",
            password="",
            salt="",
            dateInsertion="",
            dateUpdate="",
            analysis=[]):
        """
        User model used like a transfer object

        Args:
            id: User identifier
            idType: User type
            email: Email
            username: Username
            password: Password
            salt: password salt
            dateInsertion: When user was inserted
            dateUpdate: Last user update
            analysis: A list of analysis performed by user
        """
        self.id = id
        self.idType = idType
        self.email = email
        self.username = username
        self.password = password
        self.salt = salt
        self.dateInsertion = dateInsertion
        self.dateUpdate = dateUpdate
        self.analysis = analysis
