import requests, json

class languages:
	def languages():
		r = requests.get('https://emkc.org/api/v2/piston/runtime')
		langs = json.loads(r.text)
