import os
import requests


address = "1850 N 53rd st, Seattle 98103"
api_key = os.environ.get('GOOGLE_MAPS_API_KEY')
geocode_url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
url = '{0}{1}&key={2}'.format(geocode_url, address, api_key)
api_response = requests.get(url)
api_response_dict = api_response.json()

if api_response_dict['status'] == 'OK':
    latitude = api_response_dict['results'][0]['geometry']['location']['lat']
    longitude = api_response_dict['results'][0]['geometry']['location']['lng']
    print('Latitude: ', latitude)
    print('Longitude: ', longitude)
