#!/usr/bin/env python3

import sys
import algo

######################### CHECKS IF NAME EXISTS IN LIST AND RETURNS ITS POS ######################### 

def findNameInList(friendsList, name): # if it finds the name in the list of list, 
    for i in range(len(friendsList)): # else returns its index, else returns -1
        if friendsList[i][0] == name:
            return (i)
    return (-1)

######################### PRINTS USAGE ######################### 

def printUsage():
    print("""USAGE
    ./302separation file [n | p1 p2]
DESCRIPTION
    file    file that contains the list of Facebook connections
    n       maximum length of the paths
    pi      name of someone in thes file""")
    sys.exit(0)



######################### PRINTS RESULT FOR CASE ONE ######################### 

def printResultOne(friendsList):

    if findNameInList(friendsList, sys.argv[2]) == -1 or \
    findNameInList(friendsList, sys.argv[3]) == -1:
        print("Invalid input or file")
        sys.exit(84)
    else:
        nbrOfFriends = algo.nbrOfSeparation(friendsList, sys.argv[2], sys.argv[3])
        print("Degree of separation between " + sys.argv[2] + " and ", end = "")
        print(sys.argv[3] + ": " + str(nbrOfFriends))

######################### PRINTS RESULT FOR CASE TWo ######################### 

def printMatrix(friendsList, maxConnexions):
    for i in friendsList:
        for j in friendsList:
            if algo.nbrOfSeparation(friendsList, i[0], j[0]) <= maxConnexions:
                print(algo.nbrOfSeparation(friendsList, i[0], j[0]), "", end="")
            else:
                print(0, "", end="")
        print("")

def printResultTwo(friendsList):
    for i in friendsList: # prints names of matrices
        print(i[0])
    print("")
    printMatrix(friendsList, 1)
    print("")
    printMatrix(friendsList, int(sys.argv[2]))