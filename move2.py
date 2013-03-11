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

from random import randrange, uniform
import random
import glo
from ppl import makerndppl
import json
import uuid

# randrange gives you an integral value, uniform gives you a floating-point value
# frand = uniform(0, 10)

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













