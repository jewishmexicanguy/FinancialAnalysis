'''
<!DOCTYPE python>
This python file will have objects that carry out market analysis over various stocks
'''

from bet import SQL_Access
import requests
import json
import urllib

url = 'http://dev.markitondemand.com/MODApis/Api/v2/Quote/jsonp?'
ua = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'}
query = url + urllib.parse.urlencode({'symbol' : 'AAPL'}) + '&' + urllib.parse.urlencode({'callback' : 'myfunction'})
response = requests.get(query)
#print(dir(response))
print(response.text)
print(response.text)

json.loads(response.text)
for i in json.loads(response.text).keys():
    print(i)
    print(json.loads(response.text)[i])