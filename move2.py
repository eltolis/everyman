#-------------------------------------------------------------------------------
# Name:        move2
# Purpose:
#
# Author:      eapomit
#
# Created:     06/03/2013
# Copyright:   (c) eapomit 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# imports

from random import randrange, uniform
import random
import glo
from ppl import makerndppl
import json
import uuid
import sectors

# randrange gives you an integral value, uniform gives you a floating-point value
# frand = uniform(0, 10)

#---------------------------------------------------------------

# teh codez:

# case statement // for "1" return 'aaa' else 'ccc';
def f(x):
    return {
        0 : 'a warehouse',
        1 : 'a highway',
        2 : 'a forest',
        3 : 'a beach',
        4 : 'a street',
        5 : 'a farm',
        6 : 'a storage facility',
        }.get(x, 'the neverland')    # default if x not found

def see():
    print "You see ", glo.nowsee
    print "Also, you see ", glo.personList[-1].name, glo.personList[-1].job, glo.personList[-1].perks #get the lastone

# main import
def move2():
    irand = randrange(0, 7)
    #print "MoveImport " , irand #Note the comma here (not +plus), to pernei san STRING  (...cannot concatenate 'str' and 'int' objects)
    glo.nowsee=f(irand)
    #print f(irand)
    #see()
    print "You are now in ", glo.nowsee
    makerndppl()
    print "Also, you see ", glo.personList[-1].name, glo.personList[-1].job, glo.personList[-1].perks #get the lastone


                        # ... na dw meta ti ginetai me to disposal twn (un)used objects...
'''
def goHighway():
    with open('highway.loc', 'rb') as filep:
        #fortonw OLO to object.
        highway = json.load(filep)
        #fortonw MONO to object pou me endiaferei.
        nowobj = highway["objects"][random.choice(highway["objects"].keys())]
        # ean to game object einai dict,
        # prepei na akolou8ei to definition tou "karfwto",
        # allios treat it as string kai load game obj definition from file.
        if type(nowobj) == dict:
            print "   einai dictionary!", nowobj["chtoSpawn"]
        else:
            print "  ..i should load oject definition from file"
        print "   Type : " , type(nowobj) # mporei na einai type: 'dict' i 'unicode'
    #return aaa = random.choice(highway["objects"].keys())
    return nowobj
'''

def teleport():
    var = raw_input("Enter GUID: ")
    print "you entered ", var
    # ean to guid iparxei sto disko fortwse to.
    # ean oxi ftiaxto.
    #                       na dw an iparxoun gray areas fopen - fclose, performance, holes ..etc    http://effbot.org/zone/python-with-statement.htm
    try:
        with open(var + ".loc") as fileobj: pass
        print fileobj
    except IOError as e:
        print 'Oh dear.'
        guid = uuid.uuid4()
        print guid, " generated."
        # Load location template and re-save with new guid.
        with open('highway.loc', 'rb') as filep:
            #fortonw OLO to object.
            highway = json.load(filep)
        # re-save
        fname = str(guid) + ".loc"
        with open(fname, 'wb') as fp:
            # oi parametroi 8eloun sigkekrimeni seira!   http://stackoverflow.com/questions/352098/how-to-pretty-print-json-from-the-command-line
            json.dump(highway, fp, sort_keys = False, indent = 4)
        print "file Saved."


def gotoLocation(inguid):
    # OXI!---elenxei prwta gia to an iparxei to GUID.loc---
    glo.curloc = loadObjFromGUID(inguid)
    glo.urin = inguid
    print "You are now in: ", glo.urin


def loadObjFromGUID(inguid):
    # elenxei prwta gia to an iparxei to GUID.loc
    try:
        with open(inguid + ".loc") as fileobj :
            print "   Loading file " , inguid ,".loc"
            # ean uparxei, gurizei olo to object.
            return json.load(fileobj)
    except IOError as e:
        print 'loadObjFromGUID: Oh dear. You entered the astral plane! File with ', inguid ,' not Found!'
        return -1


def saveObjtoGuid(inobj, inguid):
    try:
        fname = str(inguid) + ".loc"
        with open(fname, 'wb') as fp:
            # oi parametroi 8eloun sigkekrimeni seira!   http://stackoverflow.com/questions/352098/how-to-pretty-print-json-from-the-command-line
            json.dump(inobj, fp, sort_keys = False, indent = 4)
        print "file Saved."
    except IOError as e:
        print "Error saving GUID ", inguid , "\n and object : \n", inobj

''' DEPRECATED
def updateForward(inguid):
    # epeidi pezei na ginei mlkia ama ginoun diafora events sto endiameso,
    # leo na travao to snapshot apti mnimi kai oxi apo to disko...
    # ...opote fortono to glo.curloc kai kanw overwrite to glo.guid .loc

    # pros8etw to forward
    glo.curloc["locations"] = { "forward" : inguid }
    # overwrite
    saveObjtoGuid(glo.curloc, glo.urin)
'''

def makeRndHighway(inguid):
    # san template pare to "highway"
    newobj = loadObjFromGUID("highway")
    # vale kapoia random pragmata...
    # <<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>
    # print newobj
    # efoson ola einai OK, to swzw.
    saveObjtoGuid(newobj, inguid)


def movebw():
    # Ean iparxei to KEY "back" sikw pane se auto
    if ("back" in glo.sector["points"][glo.urin]):
        # ekei pou 8elw na paw
        newguid = glo.sector["points"][glo.urin]["back"]
        # Ean den iparxei to location dimiourgise to.
        if loadObjFromGUID(newguid) == -1 :
            print "Prepei na to ftiaksw..."
            # ftiakse ena random Highway
            makeRndHighway(newguid)
            # kai pigenw ekei!
            gotoLocation(newguid)
        else :  # ean iparxei to location fortwse to.
            glo.curloc = loadObjFromGUID(newguid)
            gotoLocation(newguid)


def movefw():
    # print "XXXXXX", glo.sector["points"][glo.urin]["forward"]
    # Ean iparxei to KEY "forward" sikw pane se auto
    if ("forward" in glo.sector["points"][glo.urin]):
        # ekei pou 8elw na paw
        newguid = glo.sector["points"][glo.urin]["forward"]
        # Ean den iparxei to location dimiourgise to.
        if loadObjFromGUID(newguid) == -1 :
            print "Prepei na to ftiaksw..."
            # ftiakse ena random Highway
            makeRndHighway(newguid)
            # kai pigenw ekei!
            gotoLocation(newguid)
        else :  # ean iparxei to location fortwse to.
            glo.curloc = loadObjFromGUID(newguid)
            gotoLocation(newguid)



def initmove():
    '''
    # glo.urin = str(uuid.uuid4())
    glo.urin = "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"
    print "You begin your journey in: ", glo.urin
    gotoLocation(glo.urin)
    '''
    # kainourio
    sectors.makeSector1File()
    sectors.loadSector1()
    # valton mesa se ena tyxaio point key.
    glo.urin = random.choice(glo.sector["points"].keys())
    # print glo.urin
    # exit(0)
    print "You begin your journey in: ", glo.urin
    # ...
    # gotoLocation(glo.urin) <----------- 8a allaksw ligo ti logiki....
    # ...
    #
    # Ean den iparxei to location dimiourgise to.
    if loadObjFromGUID(glo.urin) == -1 :
        print "Prepei na to ftiaksw..."
        # kai san template pare to "highway"
        newobj = loadObjFromGUID("highway")
        # print newobj
        # efoson ola einai OK, to swzw.
        saveObjtoGuid(newobj, glo.urin)
        # kai pigenw ekei!
        gotoLocation(glo.urin)
    else :  # ean iparxei to location fortwse to.  (...mallon apo proigoumeno game...)
        glo.curloc = loadObjFromGUID(glo.urin)
        gotoLocation(glo.urin)


'''
Pleon i pliroforia gia to back/forward den 8a swzetai mesa sta guid.loc, alla sto sector1.sec
'''





