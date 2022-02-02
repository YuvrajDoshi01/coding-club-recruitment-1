import http.client
import json
import csv
import pandas as pd 
from pandas.io.json import json_normalize


#please enter the tier in words
#tier = "TIER_" + input("Enter tier : ")
tier = 'TIER_ONE'
connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': '82c61e9107cc4befaf0cce92c6fba83f' }
connection.request('GET', '/v2/competitions?plan='+tier, None, headers )
response = json.loads(connection.getresponse().read().decode())


#print (response)
jsonString = json.dumps(response)
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()

with open('data.json') as project_file:    
    data = json.load(project_file)  


#df = pd.DataFrame(data['competitions'])
#df.to_csv(r'codingclub1.csv', index=None)
#df = pd.json_normalize(data)
#df.to_csv (r'codingclub1.csv',index = None)

df = pd.json_normalize(data, 'competitions')
fields = ['id', 'name', 'area.name', 'numberOfAvailableSeasons', 'plan']
final = df.filter(fields, axis=1)
final = final.rename(
    columns={'id': 'id', 'name': 'Name', 'area.name': 'Area', 'numberOfAvailableSeasons': 'Available Seasons',
             'plan': 'Tier'})

final.to_csv(r'codingclub1.csv', index=None)
