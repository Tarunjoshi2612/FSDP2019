# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:39:14 2019

@author: Tarun Joshi
"""

# Interactive guess the number game

import random
i=0
while  i<6:
    s_number=random.randrange(1,11,)
    g_number=int(input("enter a number"))
    if type(g_number)!=int:
        print("please enter integer value")
        break
    elif s_number==g_number:
        print("player wins computer lose") 
        break
    else:
        print("player lose and computer wins")
        print("guess number={}".format(g_number))
        print("secret number={}".format(s_number))
        print("try again "+"number of tries left={}".format(5-i))
        chance=int(input("press 0 to exit any any other key to play again"))
        if chance==0:
            break
    i=i+1