from flask import Blueprint


class Group(Blueprint):
    def __init__(self, import_name: str, group_name: str, url_prefix: str):
        super().__init__(group_name, import_name, url_prefix=url_prefix)
