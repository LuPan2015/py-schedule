# encoding=utf-8

__author__ = 'pan.lu'
from Status import Status
from Types import Types
class Task:
    def __init__(self, tid, name, script, type, cron, status, start_time, end_time, parent, child, resource):
        self.tid = tid
        self.name = name
        self.script = script
        self._type = type
        self.cron = cron
        self._status = status
        self.start_time = start_time
        self.end_time = end_time
        self.parent = parent
        self.child = child
        self.resource = resource

    def status(self):
        return self.status

    @property.setter
    def status(self, status):
        if isinstance(status, Status):
            self._status = status
        else:
            raise ValueError('status must Status enum types!')

    @property
    def type(self):
        return self._type

    @property.setter
    def type(self, type):
        if isinstance(type, Types):
            self._type = type
        else:
            raise ValueError('type must Types enum type!')
