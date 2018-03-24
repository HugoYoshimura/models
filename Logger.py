import datetime


class Logger:
    def __init__(self, type='', message='', function='', obs='', config=''):
        self.type = type
        self.timestamp = str(datetime.datetime.now())
        self.function = function
        self.message = message
        self.config = config
        self.obs = obs
