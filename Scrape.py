#Author: Dominic Fate
#Desc: Code to scrape IP Unique IP addresses from Entra Sign-in logs and run them against the AbuseIPDB

import AbuseAPI

IP_set = set()

def genIPrep(IP_set):
    file = open('IP.txt', 'a')
    for ip in IP_set:
        response = AbuseAPI.API_request(ip)
        response_row = response.split(',')

        print(response_row[0])
        print(response_row[4])

        file.write(response)

    file.close()




if __name__ == '__main__':
    file_pointer = open('InteractiveSignIns_2025-08-21_2025-08-22.csv', 'r+') #download recent stuff and change this var
    filedata = file_pointer.readlines()
    for line in filedata:
        split_values = line.split(',')

        if split_values[26][1].isdigit():
            IP_set.add(split_values[26][1:-1])

    print(IP_set)
    genIPrep(IP_set)



