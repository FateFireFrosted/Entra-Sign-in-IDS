import requests
import json

def API_request(ip):
    # Defining the api-endpoint
    url = 'https://api.abuseipdb.com/api/v2/check'

    querystring = {
        'ipAddress': ip,
        'maxAgeInDays': '90'
    }

    headers = {
        'Accept': 'application/json',
        'Key': '' #define your own key
    }

    response = requests.request(method='GET', url=url, headers=headers, params=querystring)

    # Formatted output
    decodedResponse = json.loads(response.text)
    return json.dumps(decodedResponse, sort_keys=True, indent=4)

def genIPrep(IP_set):
    file = open('IP.txt', 'a')
    for ip in IP_set:
        response = API_request(ip)
        response_row = response.split(',')

        print(response_row[0])
        print(response_row[4])

        file.write(response)

    file.close()
