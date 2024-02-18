import json

with open('calendar.json') as f:
    templates = json.load(f)

print(templates)
