"""
Damilola Lawal
2040: Needle in a haystack
"""

import requests
import json

url = 'http://challenge.code2040.org/api/haystack'
data = {'token': '3ce24cfdeebac28493026ce192366d7d'}
response = requests.post(url, json = data)
response_dict = json.loads(response.text)

print(response_dict['needle'])
print(response_dict['haystack'])

#Here, the length of the haystack is traversed, the needle is found, and the
#value of the needle's address, i, is saved as index.
for i in range (len(response_dict['haystack'])):
    if response_dict['haystack'][i] == response_dict['needle']:
        index = i
        
needle_url = 'http://challenge.code2040.org/api/haystack/validate'
needle_data = {'token': '3ce24cfdeebac28493026ce192366d7d',
               'needle': index}       
needle_response = requests.post(needle_url, json = needle_data)

print(needle_response.text)

        
