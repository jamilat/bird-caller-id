import json
import requests

# read file
with open('reference.json', 'r') as f:
    data = f.read()

# parse file
obj = json.loads(data)

# show values
# print("recordings: " + str(obj['recordings']))
for rec in obj['recordings']:
    print(rec['file-name'])

    r = requests.get(rec['file'], stream = True)

    with open(rec['file-name'], 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024*1024):
            if chunk:
                f.write(chunk)

print('done')