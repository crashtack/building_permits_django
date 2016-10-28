import requests


payload = {'action_type': 'CURB CUT'}
r = requests.get('https://data.seattle.gov/resource/i5jq-ms7b.json',
                 params=payload
                 )
r.json()
