import itertools

list1 = [1,2,3]
k = 2


def combination_count (list1,k):

    #Here i get all the possible combinations of my list's shuffle.
    possibilites = list(itertools.permutations(list1))
    possibiliteslist = []
    for i in range (0,len(possibilites)):
        possibiliteslist.append(list(possibilites[i]))
    listlenght = len(list1)
    initlen = len(possibiliteslist)
    a = 0
    while listlenght != k-1:
        rank = 0
        kkk = []
        melist = []
        deepercombinationlist = []
        duplicatelist = list1
        trashlist = []
        trashbinlist = []
        for i in range (0,listlenght):
            trashlist.append(duplicatelist[i])
        if len(trashlist) == len(list1) - 1:
            qwert = 0
        elif len(trashlist) == len(list1):
            trashbinlist.append(trashlist)
        else:
            deepercombination = list(itertools.combinations(list1,len(trashlist)))
            for i in range(0, len(deepercombination)):
                deepercombinationlist.append(list(deepercombination[i]))

            for i in range(0,len(deepercombinationlist)):
                denemepermutationlist = []
                asd = deepercombinationlist[i]
                denemelist = [x for x in duplicatelist if x not in asd]
                denemepermutation = list(itertools.permutations(denemelist))
                for y in range(0, len(denemepermutation)):
                    denemepermutationlist.append(list(denemepermutation[y]))
                for u in range(0,len(denemepermutationlist)):
                    trashbinlist.append(deepercombinationlist[rank])
                rank = rank +1
                kkk = kkk + denemepermutationlist
                print trashbinlist
                print kkk
            trashbinlist = [aaa + bbb for aaa, bbb in zip(trashbinlist, kkk)]
        possibiliteslist = [x for x in possibiliteslist if x not in trashbinlist]
        a = initlen - len(possibiliteslist) - a

        listlenght = listlenght -1
    print "Possible lists that can produced with given input are: ",a
    print trashbinlist
    print len(possibiliteslist)
    print possibiliteslist
combination_count(list1,k)



