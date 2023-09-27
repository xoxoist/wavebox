from abc import ABC
from flask import Blueprint, Response, Request


class Interceptors(ABC):
    def __init__(self, path):
        pass
