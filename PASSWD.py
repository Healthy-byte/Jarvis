import os
import random
from random import choice
def passchecker(pass_input):
    passwd_liste = []
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    min_fil = os.path.join(THIS_FOLDER, 'rockyou.txt')
    fil = open(min_fil, "r", encoding="utf8")  
    
    for i in fil.readlines():
        passwd_liste.append(str(i))

    if pass_input in passwd_liste:
        print (pass_input + "\nDETTE PASSWORD ER PÅ LISTEN")
    else:
        print (pass_input + "\nDETTE PASSWORD ER IKKE PÅ LISTEN")


def passgenerator (pass_input_generate):
    tal_ekstra = []    
    store_bogstaver = "".join(choice((str.upper, str.lower))(bogstaver) for bogstaver in pass_input_generate)
    
    
    for i in range (1, 6): #tager et antal mellem 1 - 6
        print (i)
        tal_ekstra.append(random.randrange(0, 9))
      
    tal_convert = "".join(map(str, tal_ekstra))
    print("Dit nye password er: " + store_bogstaver + tal_convert)

#def passlister (minimum, maximum):
#    alfabet = "abcdefghijklmnopqrstuwvxyzæåøABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ1234567890"