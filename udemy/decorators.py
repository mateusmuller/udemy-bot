import json
import requests

class Decorators():

    @classmethod
    def pretty_json(cls, func):
        def formatter(self):
          response = requests.get (
            func(self),
            headers=self.authorization
          )
          load_json = json.loads(response.content)
          return json.dumps(load_json, indent=4, sort_keys=True)
        return formatter