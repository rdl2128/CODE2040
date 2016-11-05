"""
Damilola Lawal
2040: Registration
"""

import requests

url = 'http://challenge.code2040.org/api/register'

data = {'token': '3ce24cfdeebac28493026ce192366d7d',
          'github': 'https://github.com/rdl2128/CODE2040'}
          
response = requests.post(url, json = data)

print (response.text)
