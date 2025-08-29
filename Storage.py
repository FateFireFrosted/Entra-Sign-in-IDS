import json
import AbuseAPI

#class to store user as a json value\
class user:
    def __init__(self,login,name):
        self.login = login
        self.name = name
        self.ip_list = []

def OpenDB():
    file = open('db.json', 'r+')
    return file

def CloseDB(file):
    file.close()

def RemoveLastChar():
    file = open('db.json', 'ab+')
    file.seek(-1,2)
    file.truncate()
    file.close()

def WriteNewLogin(login,name,ip):
    RemoveLastChar()
    file = open('db.json', mode='a', encoding='utf-8')
    temp = user(login,name)
    temp.ip_list.append(ip)
    file.write(",")
    file.write(json.dumps(temp.__dict__, indent=4))
    file.write("]")
    file.close()

def UpdateDB(login,name,ip):
    file = open('db.json', 'r')
    data = json.load(file)
    if SearchDB_NewLogin(data,login):
        WriteNewLogin(login,name,ip)
    elif SearchDB_NewIP(data,ip,login):
        print("\n\n\nNEW IP for " + login + "\n")
        print(AbuseAPI.API_request(ip))
        print("\n\n\n")
    file.close()


def SearchDB_NewLogin(data,login):
    newLog = True
    for entry in data:
        if entry['login'] == login:
            newLog = False
    return newLog

def SearchDB_NewIP(data,ip,login):
    newAddress = True
    for entry in data:
        if entry['login'] == login:
            for address in entry['ip_list']:
                if address == ip:
                    newAddress = False

    return newAddress
