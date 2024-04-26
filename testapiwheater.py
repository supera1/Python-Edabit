# coding: utf-8
import requests

params = {
  'access_key': 'edd9f5e8c8bd2e6e5de6232bae39d090',
  'query': 'New York'
}

api_result = requests.get('http://api.weatherstack.com/current', params)

api_response = api_result.json()
#print(api_response)
print('Current temperature in %s is %d℃' % (api_response['location']['name'], api_response['current']['temperature']))