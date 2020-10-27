
i=1#for the game counting upto 10
u=0#for the score counting of the user
c=0#for the score counting of the computer
while(i<=10):
    print(f"Game {i}")  #for dispalying the number of game played
    s=["snake","water","gun"]
    b=int(input("enter what you want to enter\n 1) Snake 2) Water 3) Gun\n->")) #taking from user the choice
    if(b>3):#to warn the user if user enter greater number than 3
        print("Only upto 3 selection enter again")
        b=int(input("enter what you want to enter\n 1) Snake 2) Water 3) Gun -> "))
    import random as a
    d=a.choice(s) #generating the random data from s list
    print(f"-> {s[b-1]}<------>{d}")
    if((s[b-1]==s[0] and d==s[1]) or (s[b-1]==s[1] and d==s[2]) or (s[b-1]==s[2] and d==s[0])):
        u+=1#for increasing the user win point
        print(f"-> your {u} win")
        i+=1#for incresing the game lap
    elif(s[b-1]==d):
        print("draw")
        i+=1 #for incresing the game lap
    else:                                    
        c+=1 #for increasing the computer win point
        print(f"-> computer {c} win")
        i+=1  #for incresing the game lap
    print("------------------------------------------------------------------------------------")
print("your total score= ",u) #total score won by the user
print("computer total score= ",c) #total score won by the computer
if(u>c):
    print("you are the winner")
elif(u<c):
    print("computer is the winner")
else:
    print("the game is draw")

