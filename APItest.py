import json
import tensorflow as tf
import requests
import sportmonks
#soccer = SoccerApiV2(api_token='My API token')

#fixtures = soccer.fixtures_today(includes=('localTeam', 'visitorTeam'))
#for f in fixtures:
#    print(f['localTeam']['name'], 'plays at home against', f['visitorTeam']['name'])
# Get your API tokens here: https://www.sportmonks.com/settings#/api
#response = requests.get("https://soccer.sportmonks.com/api/v2.0/continents?api_token=5NQaNHaTI241kywE8HMkNY1tIRB50BwM0eiBIjHZXjeyUYZbjr9JdOBH0jDq")

#GET https://soccer.sportmonks.com/api/v2.0/leagues?api_token=__TOKEN__

#import requests

#headers = {
#    'Accept': 'application/json',
#}


response = requests.get("https://soccer.sportmonks.com/api/v2.0/head2head/18/15?api_token=xALTy37TUa1JTX6DlPHdKo5PsoLtmzxPxPZoMTHCGKXEtGRsPH6lSvou0I3r")

print(response.json())
#x = response

#y= json.loads(x)
#print(y["name"])