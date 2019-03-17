import random


builddate = []
eqrisk = []
location = []
clientid = []


def builddategenerator():
    for i in range(0,400):
        builddatee = random.randrange(1968,2018)
        builddate.append(builddatee)

def eqriskgenerator():
    for i in range(0,400):
        eqriskno = random.randrange(0,6)
        eqrisk.append(eqriskno)


def locationgenerator():
    for i in range (0,400):
        locationno = random.randrange(1,6)
        location.append(locationno)


def clientidgenerator():
    for i in range (0,400):
        clientidno = random.randrange(1,501)
        clientid.append(clientidno)

def final():
    builddategenerator()
    eqriskgenerator()
    locationgenerator()
    clientidgenerator()

final()

def txtwriter():
    if len(builddate) + len(eqrisk) + len(location)+ len(clientid)  == 1600:
        k = open("homedata.txt","w")
        for i in range (0,400):
            value = str(i+1)+","+str(builddate[i])+ "," + str(eqrisk[i])+ "," + str(location[i])+  ","+ str(clientid[i])+ "\n"
            k.write(value)
    else:
        print "ERROR"

txtwriter()