#!/usr/bin/env python3

import sys

import tools

######################### STEP 2 : delete name duplicates in [] ######################### 

def deleteDuplicate(listNames, friendsList, name1):
    isDuplicate = False
    newList = []
    
    if len(listNames) == 0:
        return(friendsList[tools.findNameInList(friendsList, name1)])
    for i in friendsList[tools.findNameInList(friendsList, name1)]:
        for j in listNames:
            if j == i:
                isDuplicate = True
        if isDuplicate == False:
            newList.append(i)
        isDuplicate = False
    return(newList)

######################### STEP 1 : checks is name1 and name2 are friends ######################### 

def findCommonFriend(friendsList, name1, name2): # with 2 names and the friends list, checks wether they are fiend or not.
    index1 = tools.findNameInList(friendsList, name1)
    
    for friend in friendsList[index1]:
        if friend == name2:
            return(True)
    return(False)

######################### STEP 0 : determines nbr of separations ######################### 

def nbrOfSeparation(friendsList, name1, name2):
    nbrOfConnexions = len(friendsList[tools.findNameInList(friendsList, name1)])
    degrees = 1
    circles = 1
    listNames = [] # Liste des personnes qu'on a vérifiés, dans l'ordre chronologique.

    if name1 == name2:
        return(0)
    elif findCommonFriend(friendsList, name1, name2):
        return(1)
    while True:
        if findCommonFriend(friendsList, name1, name2) == True:
            return(circles + 1)
        else:
            listNames.extend(deleteDuplicate(listNames, friendsList, name1)) # Ajout de personnes dans la liste.
            name1 = listNames[degrees]
            if degrees >= nbrOfConnexions:
                nbrOfConnexions = len(listNames)
                circles += 1
            degrees += 1
