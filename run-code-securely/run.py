import requests, json
class run:
	def run(code:str, version:float=3.9.4):
		data = {
			"language": 'python3',
			"version": version
			files: [
					{
						"name": "main.py",
						'content': code
					}
				],
			"run_timeout": 1000000

		}
		r = requests.post('https://emkc.org/api/v2/piston/execute', data=json.loads(data))
		response = json.loads(r.text)

		if 'message' in response:
			return 'Error: %s' % response['message']
		elif 'output' in response['run']:
			return 'Output: \n%s' % response['run']['output']


