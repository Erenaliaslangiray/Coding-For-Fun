import random
import string

plate = []
price = []
modeldate = []
accident =[]
clientid = []

letters = list(string.ascii_uppercase)
letters.remove("Q")
letters.remove("W")
letters.remove("X")

def platecreator():
    for i in range (0,700):
        a = ""
        letterno = random.randrange(1,4)
        for k in range(0,letterno):
            letterdecider = random.randrange(0,23)
            a = a + letters[letterdecider]
        plateno = random.randrange(0000,9999)
        platename = "34"+a+str(plateno)
        if platename in plate:
            platecreator()
        else:
            plate.append(platename)

def pricecreator():
    for i in range (0,700):
        pricerand = random.randrange(20000,300000)
        price.append(pricerand)

def modeldatecreator():
    for i in range (0,700):
        caryear = random.randrange(1988,2018)
        modeldate.append(caryear)

def accidentcreator():
    for i in range (0,700):
        accidentpoint = random.randrange(0,6)
        accident.append(accidentpoint)

def clientidcreator():
    for i in range (0,700):
        clientidno = random.randrange(1,501)
        clientid.append(clientidno)


def final():
    platecreator()
    pricecreator()
    modeldatecreator()
    accidentcreator()
    clientidcreator()

final()

def txtwriter():
    if len(plate) + len(price) + len(modeldate)+len(accident) + len(clientid)  == 3500:
        k = open("cardata.txt","w")
        for i in range (0,700):
            value = str(i+1)+","+plate[i]+ "," + str(price[i])+ "," + str(modeldate[i])+ ","+ str(accident[i])+ ","+ str(clientid[i])+ "\n"
            k.write(value)
    else:
        print "ERROR"

txtwriter()