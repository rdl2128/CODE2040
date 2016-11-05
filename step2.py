"""
Damilola Lawal
2040: Reverse a string
"""

import requests

url = 'http://challenge.code2040.org/api/reverse'
data = {'token': '3ce24cfdeebac28493026ce192366d7d'}
response = requests.post(url, json = data)

#Below, the given text was iterated over in reverse and saved as a new string.
reversed_text = response.text[::-1]

reversed_url = 'http://challenge.code2040.org/api/reverse/validate'
reversed_data = {'token': '3ce24cfdeebac28493026ce192366d7d',
                 'string': reversed_text}
reversed_response = requests.post(reversed_url, json = reversed_data)

print(response.text)
print(reversed_text)
print(reversed_response.text)

