import json
def get_bird_type(fullname):
    splitfn = fullname.split()
    birdtype = splitfn[len(splitfn)-1]
    return birdtype
def check_then_add(d, longname, v):
    k = get_bird_type(longname)
    if k in d:
        d[k].append(v)
    else:
        d[k] = [v]
    return d
# Opening JSON file
f = open('ref.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
# Add entries to dictionary where keys are  id's to list
birddict = {}
for r in data['recordings']:
    print('id: %s, genus: %s, species: %s, name: %s' % (r['id'], r['gen'], r['sp'], r['en']))
    birddict = check_then_add(birddict, r['en'], r['id'])

    
# Closing file
f.close()