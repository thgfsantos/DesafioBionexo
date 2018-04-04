import json
import sys


class Configuration(object):
    def __init__(self):
        pass

    def get_config(self, filename, env):
        try:
            file_ = open(filename, 'a+')
            json_string = file_.read()
            if json_string.strip():
                data = json.loads(json_string)
            return data[env]
        except Exception as error:
            print "Could not open file:", filename, error
        sys.exit()
