welc ="Welcom to currincy converter program "
print(f"{welc:*^57}")
print("")
show = False
cont= True
while cont:

    choice = input("""
    what do you want to convert :-
        1.us dollars and shekels

        2.shekels and jordanian dinars

        3.jordanian dinars and us dollars

        4. or do you want to exit
    -> """)

    def usd_nis():
        s = "converting for us dollars to shekels"
        print(f"{s:*^56}")
        usd = eval(input("enter the amount of us dollars that you want to convert to shekels -> "))
        nis= usd * 3.73
        print(f"{usd} dollars =  {nis} shekels")

    def nis_usd():
        s = "converting for shekels  to us dollars"
        print(f"{s:*^56}")
        
        nis = eval(input("enter the amount of shekels that you want to convert to us dollars -> "))
        usd = nis * 0.27
        print(f"{nis} shekels =  {usd} dollars")

    def jod_nis():
        s = "converting for jordanian dinars  to shekels"
        print(f"{s:*^62}")
        jod = eval(input("enter the amount of jordanian dinars that you want to convert to shekels -> "))
        nis = jod * 5.25 
        print(f"{jod} jordanian dinars =  {nis} shekels")

    def nis_jod():
        s = "converting for shekels  to jordanian dinars"
        print(f"{s:*^62}")
        nis = eval(input("enter the amount of shekels that you want to convert to jordanian dinars -> "))
        jod = nis * 0.19
        print(f"{nis} shekels =  {jod} jordanian dinars")    

    def jod_usd():
        s = "converting for jordanian dinars  to us dollars"
        print(f"{s:*^65}")
        jod = eval(input("enter the amount of jordanian dinars that you want to convert to shekels -> "))
        usd = jod * 1.41
        print(f"{jod} jordanian dinars =  {usd} us dollars")

    def usd_jod():
        s = "converting for us dollars to jordanian dinars"
        print(f"{s:*^65}")
        usd = eval(input("enter the amount of us dollars that you want to convert to shekels -> "))
        jod= usd *0.71
        print(f"{usd} dollars =  {jod} jordanian dinars")

    if choice == "1":
        c2 = input("""
    you want to convert :-
        1. us dollars to shekels 
        2. shekels to us dollars                                  
    -> """)
        if c2 =="1":
            usd_nis()
        elif c2 == "2":
            nis_usd()    
    elif choice == "2":
        c2 = input("""
    you want to convert :-
        1. jordanian dinars to shekels 
        2. shekels to us jordanian dinars                                  
    -> """)
        if c2 =="1":
            jod_nis()
        elif c2 == "2":
            nis_jod()
    elif choice == "3":
        c2 = input("""
    you want to convert :-
        1. jordanian dinars to dollars
        2. dollars to us jordanian dinars                                  
    -> """)
        if c2 =="1":
            jod_usd()
        elif c2 == "2":
            usd_jod()        
    elif choice ==  "4":
        print("program ended")
        quit()
    else:
        show = True
        print("invalid choice try again ")

    if show == False:
        qq= input("do you want to continue thr program (yes/no) \n")
        if qq == "yes".lower():
            choice = True
        elif qq == "no".lower():
            choice = False
            print("program ended")
            quit()






        





