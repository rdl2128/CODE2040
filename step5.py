"""
Damilola Lawal
2040: Dating Game
"""

import requests
import json
import dateutil
import datetime

url = 'http://challenge.code2040.org/api/dating'
data = {'token': '3ce24cfdeebac28493026ce192366d7d'}
response = requests.post(url, json = data)
response_dict = json.loads(response.text)

datestamp = response_dict['datestamp']
interval = response_dict['interval']
parsed_date = dateutil.parser.parse(datestamp, parserinfo=None)

#The result of the interval added to the datetime taken from the dictionary is
#saved as a new datetime and put into the given ISO 8601 format
updated_stamp = (parsed_date + datetime.timedelta(0,interval)).isoformat()
updated_stamp = str(updated_stamp).replace('+00:00', 'Z')

updated_url = 'http://challenge.code2040.org/api/dating/validate'
updated_data = {'token': '3ce24cfdeebac28493026ce192366d7d', 
                'datestamp': updated_stamp}
updated_response = requests.post(updated_url, json = updated_data)

print(datestamp, '\t', interval)
print (updated_stamp, '\t', updated_response.text)
