from datetime import datetime
from data_types.content import Content

class Task:
    def __init__(self, name: str, end_time: datetime, content: Content):
        self._name = name
        self._end_time = end_time
        self._content = content

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value: datetime):
        self._end_time = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value: Content):
        self._content = value
