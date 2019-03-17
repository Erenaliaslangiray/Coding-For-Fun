
#Illness Value (0-10), Age (18-100)
Client = [3, 35]

#Illness Value (0-10), Age, Family Degree (1-2)1:Wife 2:Kid
Family = [[2,7,2],[3,32,1]]

#Car Value (Max 300.000 TL) Best when its low, Car Purchase Year (Max 30 years old cars), Car Accident Value (0-5) Note: Car accident value is best when its low.
Car = [[120000,2010,2]]

#Home Year (Max 50 years old houses), Earthquake Risk (0-5), Home Location (1-5)
Home = [[1998,3,5]]


def algh ():
    riskcolors = ["Green", "Blue", "Yellow", "Red", "Black"]
    Clen = 1
    Flen = len(Family)
    Carlen = len(Car)
    Hlen = len(Home)

    k = (4.0 * Clen) + (3.0 * Flen) + (2.0 * Carlen) + (3.0 * Hlen)
    x = 100.0/k

    x_clen = (x * Clen * 4)/100
    x_flen = (x * Flen * 3)/100
    x_carlen = (x * Carlen * 2)/100
    x_hlen = (x * Hlen * 3)/100

    #Client Risk Calculation
    crisk = ((0.6 * (Client[0]/10.0)) + (0.4 * (Client[1]/100.0)))
    cfinal = (crisk*0.9 + 0.06) * x_clen

    #Family Risk Calculation
    if x_flen ==0:
        ffinal = 0
    else:
        frisk = 0
        for i in range(0,Flen):
            frisk = frisk + (0.7 * (Family[i][0]/10.0) + (0.2 * (Family[i][1]/100.0)) + (0.1 * ((3 - Family[i][2])/2.0)))

        frisk = (frisk / Flen) + ((Flen -1) * 0.05 )
        ffinal = (frisk * 0.9 + 0.06) * x_flen

    #Car Assets Risk Calculation
    if x_carlen == 0:
        carfinal = 0
    else:
        carrisk = 0
        for i in range(0,Carlen):
            carrisk = carrisk + (0.6 * (Car[i][0]/300000.0) + (0.2 * ((2018 - Car[i][1])/30.0)) + (0.2 * ((5 - Car[i][2])/5.0)))

        carrisk = (carrisk / Carlen) + ((Carlen -1) * 0.05 )
        carfinal = (carrisk * 0.9 + 0.06) * x_carlen


    #House Assets Risk Calculation
    if x_hlen == 0:
        hfinal = 0
    else:
        hrisk = 0
        for i in range(0,Hlen):
            hrisk = hrisk + (0.3 * (2018-Home[i][0])/50.0) + (0.4 * ((Home[i][1])/5.0)) + (0.3 * ((Home[i][2])/5.0))

        hrisk = hrisk / Hlen  + ((Hlen -1) * 0.05 )
        hfinal = (hrisk * 0.9 + 0.06) * x_hlen

    risktotal = cfinal + ffinal + carfinal + hfinal

    riskprintvalue = risktotal * 100
    Riskcolorvalue = risktotal * 5
    colorselect = int(Riskcolorvalue)
    print "Policy risk level is:", riskprintvalue
    print "Policy risk color is:", riskcolors[colorselect]

algh()


