"""
Damilola Lawal
2040: Prefix
"""

import requests
import json

url = 'http://challenge.code2040.org/api/prefix'
data = {'token': '3ce24cfdeebac28493026ce192366d7d'}
response = requests.post(url, json = data)
response_dict = json.loads(response.text)

prefix = response_dict['prefix']
sans_prefix = []

#The array of strings is traversed, each string is checked to see if it starts
#with the given prefix, and if that is not the case, it is added to the new
#array declared above for strings without the prefix
for element in response_dict['array']:
    if (element.startswith(prefix) == 0):
        sans_prefix.append(element)
        
sans_url = 'http://challenge.code2040.org/api/prefix/validate'
sans_data = {'token': '3ce24cfdeebac28493026ce192366d7d',
             'array': sans_prefix}
sans_response = requests.post(sans_url, json = sans_data)

print(response.text)
print(sans_prefix)
print(sans_response.text)
