import pandas as pd
from pathlib import Path
import json

# file is in current dir
path = Path(r'calendar.json')

# read json
with path.open('r', encoding='utf-8') as f:
    data = json.loads(f.read())

# create dataframe
df = pd.json_normalize(data)

# save to csv
df.to_csv('test.csv', index=False, encoding='utf-8')  

