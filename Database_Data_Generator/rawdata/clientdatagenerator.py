import random
import re

text_file = open("name_surname.txt", "r")
data = text_file.read()
name_surname = re.split(" |\n",data)


TC = []
name = []
surname = []
mail = []
phone = []
password = []
birthdate = []
birthdatex = []
birthdatef = []
Healthrisk = []
clientid = []
relationid = []
relationdict = {}


def tccreator ():
    for i in range (0,1000):
        tcno = random.randrange(10000000000,99999999999)
        while tcno in TC:
            tcno = random.randrange(10000000000,99999999999)
        TC.append(tcno)

def namecreator ():
    for i in range (0,2000,2):
        name.append(name_surname[i])

def surnamecreator ():
    for i in range(1,2000,2):
        surname.append(name_surname[i])

def mailcreator ():
    for i in range (0,500):
        m = surname[i]+"@gmail.com"
        while m in mail:
            m = surname[i]+"1"+"@gmail.com"
        mail.append(m)

def phonecreator():
    for i in range (0,1000):
        telno = random.randrange(100000000,999999999)
        telnof = "05" + str(telno)
        while telnof in phone:
            telno = random.randrange(100000000, 999999999)
            telnof = "05" + str(telno)
        phone.append(telnof)

def passcreator():
    for i in range (0,500):
        passcode = name[i]+surname[i]+"123"
        password.append(passcode)

def birthdatecreator():
    for i in range (0,500):
        day = random.randrange(1,31)
        month = random.randrange(1,13)
        year = random.randrange(1918,1989)
        date = str(day) + "/" + str(month) + "/" + str(year)
        datex = year
        birthdate.append(date)
        birthdatex.append(datex)


def healthriskcreator():
    for i in range (0,1000):
        hrisk = random.randrange(0,11)
        Healthrisk.append(hrisk)

def clientidcreator():
    for i in range (0,500):
        clientidno = random.randrange(1,501)
        clientid.append(clientidno)

def dictcreator():
    for i in range (0,500):
        x = clientid[i]
        if x in relationdict.keys():
            a = relationdict[x]
            relationdict[x] = a+1
            relatid = 2
            relationid.append(relatid)
        else:
            relationdict[x] = 1
            relatid = 1
            relationid.append(relatid)


def birthdatefamilycreator():
    for i in range(0,500):
        if relationid[i] == 1:
            x = clientid[i]-1
            y = birthdate[x]
            z = y[-4:]
            c = int(z)
            day = random.randrange(1, 31)
            month = random.randrange(1, 13)
            year = random.randrange(c-5, c+6)
            date = str(year)
            birthdatef.append(date)
        elif relationid[i] == 2:
            day = random.randrange(1, 31)
            month = random.randrange(1, 13)
            year = random.randrange(2000,2018)
            date = str(year)
            birthdatef.append(date)

def finalcreator():
    tccreator()
    namecreator()
    surnamecreator()
    mailcreator()
    phonecreator()
    passcreator()
    birthdatecreator()
    healthriskcreator()
    clientidcreator()
    dictcreator()
    birthdatefamilycreator()

finalcreator()

def txtwriter():
    if len(TC) + len(name) + len(surname) + len(mail) + len(phone) + len(password) + len(birthdatex) + len(Healthrisk) == 6500:
        k = open("clientdata.txt","w")
        for i in range (0,500):
            value = str(i+1)+","+str(TC[i])+ "," + name[i]+ "," + surname[i]+ ","+ mail[i]+ "," + phone[i] + ","+ password[i]+ ","+ str(birthdatex[i])+ ","+ str(Healthrisk[i]) + "\n"
            k.write(value)
    else:
        print "ERROR"
        print len(TC) + len(name) + len(surname) + len(mail) + len(phone) + len(password) + len(birthdate) + len(Healthrisk)

txtwriter()





def txtwriterfam():
    k = open("familydata.txt", "w")
    for i in range(500, 1000):
        value = str(i-499)+","+str(TC[i]) + "," + name[i] + "," + surname[i] + "," + phone[i] + "," + str(relationid[i-500]) + "," + str(Healthrisk[i]) + "," + str(birthdatef[i-500])+ "," + str(clientid[i-500])+ "\n"
        k.write(value)

txtwriterfam()