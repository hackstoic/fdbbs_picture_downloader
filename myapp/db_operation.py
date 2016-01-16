# encoding=utf8

import os
import shelve


class DBOperation(object):
    @classmethod
    def get_urls(cls):
        pass

    @classmethod
    def update_urls(cls):
        pass

    @classmethod
    def isVisited(cls):
        pass


class ShelveOperation(object):
    def __init__(self):
        self.db_file = os.path.join(os.path.split(os.path.realpath(__file__))[0], "myapp.db")
        self.s = shelve.open(self.db_file)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.s.close()
        return True

    def update_db(self, key, value):
        self.s[key] = value
        return True

    def get_value_by_key(self, key):
        value = self.s.get(key)
        return value

    def get_all_values(self):
        return self.s.iteritems()

    def reset_db(self):
        keys = self.s.iterkeys()
        for key in keys:
            del self.s[key]
        return True