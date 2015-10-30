"""
Goal: represent a publisher object
"""


class Publisher(object):

    def __init__(self, json):
        self.last_status_check_time = json['last-status-check-time']
        self.primary_name = json['primary-name']
        self.counts = json['counts']
        self.prefix = json['prefix']
        self.tokens = json['tokens']
        self.names = json['names']
        self.location = json['location']
        self.id = json['id']

    def to_string(self):
        primary_name = self.primary_name.encode('utf-8') \
            if self.primary_name is not None else ''
        location = self.location.encode('utf-8')
        string = "[{}] {} \n\tLocation: {}"\
            .format(self.id, primary_name, location)
        return string
