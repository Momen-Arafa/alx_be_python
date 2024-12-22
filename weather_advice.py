# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 22:37:08 2024

@author: mimo3
"""
Right_Move = "4"
Your_Move = ""
number_of_moves = 0
move_limit = 3
out_of_moves = False

while Your_Move != Right_Move and not(out_of_moves):
    if number_of_moves <= move_limit:
      Your_Move = input("still lost your move : ")
      number_of_moves += 1
    else:
        out_of_moves = True
if out_of_moves:
    print("out of moves! you died!")
else:    
    print( "horay! found the door")
                