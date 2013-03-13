#-------------------------------------------------------------------------------
# Name:        everyman
# Purpose:
#
# Author:      eapomit
#
# Created:     06/03/2013
# Copyright:   (c) eapomit 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# imports
    # from <filename> <import function>
from move2 import move2, see, teleport, movefw, initmove, movebw
import glo                                  #gia ta glo prepei na to kanw etsi (xoris to from .. import * ) giati den douleuei    http://stackoverflow.com/questions/142545/python-how-to-make-a-cross-module-variable
#import ppl
from ppl import *

# ------------------------------
def move():
    print "You moved!"

# inits //logika DEN prepei na ginontai inits sto glo.py
nowsee=""
initmove()

# main loop
while 1:
    var = raw_input("Enter something: ")
    print "you entered ", var
    if var=="q": break;
    #if var=="m": move()
    if var=="w": move2()                # will be deprecated, along with f(x)
    if var=="s": see()
    if var=="c": chat()
    if var=="p": print getRndPerk()
#    if var=="l": print goHighway()     # deprecated
    if var=="t": teleport()             # will be replaced
    if var=="f": movefw()
    if var=="b": movebw()

# exit main loop
print "Good bye!"


'''
8a to kanw me "themes" diladi 8a kano init ena "highway" kai auto mesa 8a exei location alla 2-3 highways
+ small %%% to "forest", etc.   ...
"Walk to :
    1) highway (continue onto the highway)
    2) highway (On the side, you see a forest (on the horizon/ in the distance / not faraway from here / nearby )"
    3) highway (turn back)

1) init completely new "highway" from template. (special events from previous encounters may occur though: .. You moved towards the highway. The zombies have stopped following you. You see a... )
2)
3) load previous location(guid). Note: to kserei giati otan ftiaxtei auto to instance 8a prepei kapos na pernaw san
    parametro oti auta ta 2 sindeontai.

pipeline:
load game
init location from template ( %forward, %backward, %else, ..etc )
    ??? init nextmove() locations ???
player actions into location
move2()

earlypipe:
    from_guid = getguid()
    new make('highway.loc', from_guid)
    mesa sto highway.loc 100% chtogoHighway ( gia to 1) )
    ean patisei 1)
        save from_guid.sloc
        make('highway.loc', from_guid)
        from_guid = getguid()


moveto(guid)
    ean to guid iparxei sto disko fortwse to.
    ean oxi ftiaxto.



map:
You were on your way to
    Atlanta/Wiskonsin/Wasinghton city
to
    meet your parents / for lunch / pick up your kid from school / get your brother out of jail...
    (get medication for your mother.  the farmacy is west from here. your house is east from here.)
You know that ... is west from here.



'''



