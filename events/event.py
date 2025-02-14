from datetime import datetime, timedelta
from data_types.content import Content
from data_types.location.even_location import EvenLocation
from data_types.participants import Participants
from data_types.task import Task


class Event:
    def __init__(self, name: str, start_date: datetime, duration: timedelta, content: Content, ev_location: EvenLocation,
                 participants: Participants, tasks: list[Task]):
        self._name = name
        self._start_date = start_date
        self._duration = duration
        self._content = content
        self._ev_location = ev_location
        self._participants = participants
        self._tasks = tasks
        self._content_is_hide = False

    def hide_content(self):
        self._content_is_hide = True

    def un_hide_content(self):
        self._content_is_hide = False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value: datetime):
        self._start_date = value

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value: timedelta):
        self._duration = value

    @property
    def content(self):
        if not self._content_is_hide:
            return self._content
        else:
            raise AttributeError("Access to content is not allowed now")

    @content.setter
    def content(self, value: Content):
        self._content = value

    @property
    def ev_location(self):
        return self._ev_location

    @ev_location.setter
    def ev_location(self, value: EvenLocation):
        self._ev_location = value

    @property
    def participants(self):
        return self._participants

    @participants.setter
    def participants(self, value: Participants):
        self._participants = value

    @property
    def tasks(self):
        return self._tasks

    @tasks.setter
    def tasks(self, value: list[Task]):
        self._tasks = value
