#-------------------------------------------------------------------------------
# Name:        glo
# Purpose:
#
# Author:      eapomit
#
# Created:     06/03/2013
# Copyright:   (c) eapomit 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#from ppl import Person

nowsee="shit"

# to GUID tou location pou vriskesai TWRA
urin = 0

# o Sector pou vrisketai autin tin stigmi o paixtis.
sector = {}

# ena sector apoteleitai apo polla locations (i allios points)

# to OBJECT tou location pou vriskesai TWRA. Prepei na eguatai oti einai to TWRINO location,
# kai prepei na ginetai update mono AFOU allaksei to location.
# (p.x. oxi na ginei update kata la8os gia ena aplo var check!!!)
curloc = {}


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

#create an empty list with all the people that have appeared in the game.
personList = []
#create the class instances ON DEMAND!
