#-------------------------------------------------------------------------------
# Name:        ppl
# Purpose:
#
# Author:      eapomit
#
# Created:     06/03/2013
# Copyright:   (c) eapomit 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import glo
import random
from random import randrange, uniform
import json

'''
# ==============================================================================
# these are immutable vars. I will not be using SETS or dictionaries, instead i will use a combination of immut.vars &
# for PERKS i could use for volatility: A LIST as stack or queue and
#                                       append, remove members and
#                                       check for membership with count"occurance" > 1
#                                       OR use a SET for more strict code and easy access with 'orange' in fruit.
#                                       ( x in s, add(x), discard(x) )

#                                       telika lew anti gia SET na xrisimopoiisw ena DICTIONARY
#                                       kai na checkarw gia membership me:   if key in array:  OR ( http://stackoverflow.com/questions/3845362/python-how-can-i-check-if-the-key-of-an-dictionary-exists    )
#                                                                       (i gia multiple values     http://stackoverflow.com/questions/6159313/can-python-test-the-membership-of-multiple-values-in-a-list   )
#                                       kai opou den xreiazetai pair Key : Value 8a vazw Value = -1
#                                       8a to xrisimopoiw diladi to Key gia to PERK kai to Value gia to PROPERTY
#                                       to dictionary den exei add()    http://stackoverflow.com/questions/1024847/add-to-a-dictionary-in-python

name="babuski"
prof=""
hobby=""
gender=""
age=0 # desc: little / young / boy / girl / child / teenager / mid'30s / 40s / 50ish / old
# kai ta PERKS 8a einai mia lista pou 8a vazw/vgazo "hasguntraining", "gunproficient", ...
# kai 8a elenxw me if isinlist"gunproficient"...
myset={"hasguntraining", "gunproficient"}
'''


class Person(object):
    def __init__(self, name=None, job=None, hobby=None, gender=None, age=None, perks={}):
        self.name = name
        self.job = job
        self.hobby = hobby
        self.gender = gender
        self.age = age
        self.perks = perks

'''
#create an empty list
personList = []
#create two class instances
personList.append(Person("Payne N. Diaz", "coach", "baseball", "Male", 45))
personList[0].perks={"hasguntraining", "gunproficient"}
personList.append(Person("Mia Serts", "bicyclist", "rpgs", "Female", 22))
personList[1].perks={"pretty"}

print personList[0].perks
'''

'''
glo.personList.append(Person("Payne N. Diaz", "coach", "baseball", "Male", 45))
glo.personList[0].perks={"hasguntraining", "gunproficient"}
glo.personList.append(Person("Mia Serts", "bicyclist", "rpgs", "Female", 22))
glo.personList[1].perks={"pretty"}
'''


# ==============================================================================

def chat():
    print "You approach ", name
    print "a) ask to join your group. "
    var = raw_input()
    if var=="a": print "You asked ", name ," to join your group."

'''
    DESC example:
    You see a tall/black/handsome/man/woman in his/her mid30's
    He/she seems worried/distracted/ to be crying/ to be ignoring you/ is starring at you/ smiles at you/
    seems occupied with/ is trying to...

    c:chat
    9/10 You learned that his/her name is .. acknwoledged=1

    Next time in SEE() instead of DESC() "You see NAME."

    SEE(0x0001) pplinstance. If acknwoledged=1 "You see NAME." else DESC(0x0001)

'''

# DESC() a person displaying what YOU currently know about him/her.
def desc(ppl):
    print "lalala"

# DESC() a person displaying ALL instance stats.
def deschack(ppl):
    print "lilili"

''' deprecated...
def getMaleName(x):
    return {
        0 : 'Jim',
        1 : 'Lee',
        2 : 'Tony',
        3 : 'Stam',
        4 : 'George',
        5 : 'John',
        6 : 'Tol',
        }.get(x, 'the NoName')    # default if x not found
'''

def getMaleName():
    fileName=open("MaleName.txt")
    lines = [i.strip() for i in fileName.readlines()] #pinakas lines
    name=lines[randrange(0, len(lines))] # +1 -1??? nooooot
    return name

def getFemaleName():
    fileName=open("FemaleName.txt")
    lines = [i.strip() for i in fileName.readlines()] #pinakas lines
    name=lines[randrange(0, len(lines))] # +1 -1??? nooooot
    return name

# JOBS ===========================================================

def getMaleJob():
    fileName=open("MaleJob.txt")
    lines = [i.strip() for i in fileName.readlines()] #pinakas lines
    job=lines[randrange(0, len(lines))] # +1 -1??? nooooot
    return job

def getFemaleJob():
    fileName=open("FemaleJob.txt")
    lines = [i.strip() for i in fileName.readlines()] #pinakas lines
    job=lines[randrange(0, len(lines))] # +1 -1??? nooooot
    return job

def getUniJob():
    fileName=open("UniJob.txt")
    lines = [i.strip() for i in fileName.readlines()] #pinakas lines
    job=lines[randrange(0, len(lines))] # +1 -1??? nooooot
    return job

def getJob(gender):
    irand = randrange(0, 3) # 0,1,2
    if (irand==0 or irand==1) and gender=="Male":
        return getMaleJob()
    elif (irand==0 or irand==1) and gender=="Female":
        return getFemaleJob()
    else:
        return getUniJob()
    print "neverlaaaaaand"

                            # !!!!!!! ...kano fopen na dw pote prepei na ta kleinw kiolas kai na destroy to object???

def getRndPerk():
    with open('perks.json', 'rb') as filep:
        perks = json.load(filep)
    return random.choice(perks.keys())

def makerndppl():
    gender=""
    name=""
    age=randrange(10, 80)
    irand = randrange(0, 2)
    if irand==1:
        gender="Male"
        name=getMaleName()
    else:
        gender="Female"
        name=getFemaleName()
    glo.personList.append( Person(name, getJob(gender), "balll", gender, age, getRndPerk()) )
    #{"key1" : "value1", "key2" : "value2"}))









