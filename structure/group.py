from flask import Blueprint
import random


class Group(Blueprint):
    def __init__(self, import_name: str, group_name: str, url_prefix: str):
        all_numbers = list(range(100, 1000))
        random.shuffle(all_numbers)
        unique_numbers = all_numbers[:10][0:1][0]
        super().__init__(name="{}_{}".format(group_name, unique_numbers),
                         import_name=import_name,
                         url_prefix=url_prefix)
