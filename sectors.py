#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      eapomit
#
# Created:     13/03/2013
# Copyright:   (c) eapomit 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# imports

import glo
import random
from random import randrange, uniform
import json
import uuid

#------------------------------------------------------

def getRndSector(inpoints, innodes):
    #---, inFilename):---
    # inpoints 8a pernao posa points 8elw na exei to sector (poso "megalo" 8a einai ena "lvl")
    # innodes 8a einai ena ---SET--- LIST apo guids ta opoia 8a diamoirazontai tyxaia mesa sta points tou sector
    # kai 8a apoteloun external nodes (ektos apo ta forward and back).
    # auta ta guids mallon 8a mpoune se ena arxeio ws "Pending sectors to be spawned"
    # ..logika 8a mpei kai kapoios elenxos giati mporei i lista na exei polles fores to idio guid
    # wste na mporeis na mpeis na mpeis se ena sector apo polla nodes?
    # (more accurate example could be a cave entrance, you could enter from: up a hill OR down a mountain)
    sector = {}
    sector["name"] = "sector1"
    sector["points"] = {}
    # sector["points"]["forward"] = {}
    # sector["points"]["back"] = {}
    # sector["points"][""] = {}

    now = str(uuid.uuid4()) # initial point
    nxt = str(uuid.uuid4())
    prev = ""
    for i in range(inpoints):
        # ean eisai stin arxi
        if prev == "":
            # update mono nxt
            # sector["points"].update({ now : nxt })               # add a string
            sector["points"].update({now : {} })
            sector["points"][now]["forward"] = nxt
        else:
            if i == inpoints - 1 : # ean einai sto "telos" update mono prev
                # sector["points"].update({ now : prev })          # add a string
                sector["points"].update({now : {} })
                sector["points"][now]["back"] = prev
            else: # ean einai sti "mesi" update prev + nxt
                # sector["points"].update({ now : [ prev, nxt ] }) # add a list
                sector["points"].update({now : {} })
                sector["points"][now]["back"] = prev
                sector["points"][now]["forward"] = nxt
        prev = now
        now = nxt
        nxt = str(uuid.uuid4())
    return sector

def makeSector1File():
    sector = getRndSector(5, 0)
    try:
        fname = "sector1.sec"
        with open(fname, 'wb') as fp:
            # oi parametroi 8eloun sigkekrimeni seira!   http://stackoverflow.com/questions/352098/how-to-pretty-print-json-from-the-command-line
            json.dump(sector, fp, sort_keys = False, indent = 4)
        print "sector1.sec saved."
    except IOError as e:
        print "Error saving sector1.sec with sector: \n ", sector


def loadSector1():
    try:
        with open("sector1.sec") as fileobj :
            print "Opening sector1.sec"
            glo.sector = json.load(fileobj)
    except IOError as e:
        print 'Error opening sector1.sec"'



