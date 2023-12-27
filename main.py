import requests
import json
import sys
import os



# Get arguments from command line and store them in a list
args = sys.argv[1:]
configFile = 'config.json'


if len(args) == 0:
    print("Using default config file: config.json")
else:
    configFile = args[0]

if not os.path.isfile(configFile):
    print("Config file not found")
    exit()

# Open config file and load it into a dictionary
with open(configFile) as json_file:
    config = json.load(json_file)

cookies = {
    'namebase-main': config['namebaseToken']
}
headers = {'Content-Type': 'application/json'}
data = {
    'bidAmount': config['bid'],
    'blindAmount': config['blind']
}

# Loop for count domains
start = config['start']
number = config['count']
# Create list of domains using prefix and number
padding = len(str(number))
print(data)

for i in range(number):
    domain = config['prefix'] + str(i).zfill(padding)
    print("Bidding on: " + domain)

    response = requests.post('https://www.namebase.io/api/v0/auction/' + domain + '/bid', cookies=cookies,headers=headers, json=data)
    print(response.text)
    if response.status_code != 200:
        print("Error bidding on: " + domain)
        print(response.text)
        exit()