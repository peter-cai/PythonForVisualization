import requests,pdb

url = 'http://github.com/time.json'

r = requests.get(url)
json_obj = r.json()

repos = set()
for entry in json_obj:
	try:
		#pdb.set_trace()
		repos.add(entry['repository']['url'])
	except KeyError as e:
		print("No key %s. Skipping..."%(e))

from pprint import pprint
pprint(repos)			