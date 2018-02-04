import datetime


def Logger:
    def __init__(self, message='', function='', obs='', config=''):
        self.timestamp = str(datetime.datetime.now())
        self.function = function
        self.message = message
        self.config = config
        self.obs = obs
