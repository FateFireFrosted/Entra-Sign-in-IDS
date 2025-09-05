import json
import sys

#To whitelist a new IP run py whitelist.py <login> <IP>
def Whitelist(login,ip):
    file = open("db.json", "r+")
    data = json.load(file)
    newAddress = True
    for entry in data:
        if entry['login'] == login:
            print("Found User")
            for address in entry['ip_list']:
                if address == ip:
                    newAddress = False
                    print("IP already exists in whitelist for current User")
            if newAddress == True:
                entry['ip_list'].append(ip)
                print("Adding IP to Whitelist")
                file.close()
                file = open("db.json", "w")
                file.write(json.dumps(data, indent=4))
                file.close()
                print("Updated Whitelist")

def main(login,ip):
    Whitelist(login,ip)

if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])