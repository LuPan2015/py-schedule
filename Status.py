# encoding=utf-8

__author__ = 'pan.lu'
from enum import Enum

class Status(Enum):
    Waiting = 0  # 调度未到或依赖未满足
    Pending = 1  # 等待资源
    Running = 2  # 运行中
    Success = 3  # 运行成功
    Failed = 4  # 运行失败
