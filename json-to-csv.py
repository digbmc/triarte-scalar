"""
To do:
- Load Triarte json
- Iterate through objects and grab metadata
- Rename categories as scalar labels
- Output to csv

"""

import json


f = open('double-take-tri.json')
data = json.load(f)