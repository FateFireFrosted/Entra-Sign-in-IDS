#Author: Dominic Fate
#Desc: Code to scrape IP Unique IP addresses from Entra Sign-in logs and run them against the AbuseIPDB

import AbuseAPI
import sys

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


def main():

    try:
        file_pointer = open(sys.argv[1], 'r+') #download recent stuff and change this var
        filedata = file_pointer.readlines()
        for line in filedata:
            split_values = line.split('","')
            if split_values[25][1].isdigit():
                IP_set.add(split_values[25])

        print(IP_set)
        genIPrep(IP_set)
    except FileNotFoundError:
        print(f"Error: The file '{sys.argv[1]}' was not found.")
    except IOError as e:
        print(f"Error opening or reading file '{sys.argv[1]}': {e}")



if __name__ == '__main__':
    main()