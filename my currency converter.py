#import os module
import os

# define the converter function.
def converter():

    #to check if input was a valid number
    while True:
        try:
            Cnumber = float(input("Input amount to convert from/to. --> "))
            break

        except (ValueError, TypeError, NameError, RuntimeError):
            print(" \n Ooops ! That was not a valid number. Try again... -->")
            converter()
            break


    #get type input
    Ctype = input("Input converson type here ---> ")
    Ctype = Ctype.upper()

    #to check if input was a valid type
    #open the rates text file and read parameters
    Rates = open("Rates.txt","r",)


    for line in Rates:

        feilds = line.split(";")
        Ratename = feilds[0]
        Ratevalue = feilds[1]

        # to check for the particular rate selected and perform conversion
        if Ratename == Ctype:
            print (Ratename)
            print(Ratevalue)


            Cconverted = float(Cnumber) * float(Ratevalue)


            # Output Reply
            if  "DY" == Ctype :
                print ("\n")
                print (str(Cnumber) + " Dollar(s) is equal to  " + str(Cconverted) + "  Yen \n" )
            elif "DP" == Ctype:
                print ("\n")
                print (str(Cnumber) + " Dollar(s) is equal to  " + str(Cconverted) + "  Pound(s) \n" )
            elif "DE" == Ctype:
                print ("\n")
                print (str(Cnumber) + " Dollar(s) is equal to  " + str(Cconverted) + "  Euro(s) \n" )
            elif "DN" == Ctype:
                print ("\n")
                print (str(Cnumber) + " Dollar(s) is equal to  " + str(Cconverted) + "  Naira \n" )
            elif "PD" == Ctype:
                print ("\n")
                print (str(Cnumber) + " Pound(s) is equal to  " + str(Cconverted) + "  Dollar(s) \n" )
            elif "PE" == Ctype:
                print ("\n")
                print (str(Cnumber) + " Pound(s) is equal to  " + str(Cconverted) + "  Euro(s) \n" )
            elif "PN" == Ctype:
                print ("\n")
                print (str(Cnumber) + " Pound(s) is equal to  " + str(Cconverted) + "  Naira \n" )
            elif "PY" == Ctype:
                print ("\n")
                print (str(Cnumber) + " Pound(s) is equal to  " + str(Cconverted) + "  Yen \n" )
            elif "ED" == Ctype:
                print ("\n")
                print (str(Cnumber) + " Euro(s) is equal to  " + str(Cconverted) + "  Dollar(s) \n" )
            elif "EP" == Ctype:
                print ("\n")
                print (str(Cnumber) + " Euro(s) is equal to  " + str(Cconverted) + "  Pound(s) \n" )
            elif "EN" == Ctype:
                print ("\n")
                print (str(Cnumber) + " Euro(s) is equal to  " + str(Cconverted) + "  Naira \n" )
            elif "EY" == Ctype:
                print ("\n")
                print (str(Cnumber) + " Euro(s) is equal to  " + str(Cconverted) + "  Yen \n" )
            elif "YD" == Ctype:
                print ("\n")
                print (str(Cnumber) + " Yen is equal to  " + str(Cconverted) + "  Dollar(s) \n" )
            elif "YP" == Ctype:
                print ("\n")
                print (str(Cnumber) + " Yen is equal to  " + str(Cconverted) + "  Pound(s) \n" )
            elif "YE" == Ctype:
                print ("\n")
                print (str(Cnumber) + " Yen is equal to  " + str(Cconverted) + "  Euro(s) \n" )
            elif "YN" == Ctype:
                print ("\n")
                print (str(Cnumber) + " Yen is equal to  " + str(Cconverted) + "  Naira \n" )
            elif "ND" == Ctype:
                print ("\n")
                print (str(Cnumber) + " Naira is equal to  " + str(Cconverted) + "  Dollar(s) \n" )
            elif "NP" == Ctype:
                print ("\n")
                print (str(Cnumber) + " Naira is equal to  " + str(Cconverted) + "  Pound(s) \n" )
            elif "NE" == Ctype:
                print ("\n")
                print (str(Cnumber) + " Naira is equal to  " + str(Cconverted) + "  Euro \n" )
            elif "NY" == Ctype:
                print ("\n")
                print (str(Cnumber) + " Naira is equal to  " + str(Cconverted) + "  Yen \n" )
                break

            break
    Rates.close()



# project to build a currency converter
#define how to collect inputs
#ask the type of conversion to undergo
print ("\n Welcome, Please select the currencies you'd wish to convert to/from. \n")
print ("Legend \n D -- U.S Dollar ($) \n P -- Pound Sterling (P) \n E -- Euro (E) \n Y -- Chinese Yen (Y)")
print ("\nExample: For conversion from Dollar (D) to Naira (N) : \n      conversion type will be --> DN \n")

active = 1

#app process
while active == 1 :

    #call up the converter function.
    converter()

    ContinueRunning = input("Do you wish to perform aother conversion --> Y [yes]/ N [no] --->").lower()

    if ContinueRunning == "y":
        active = 1
    elif ContinueRunning == "n":
        active = 0
        print (" \n Thanks for using the app, Goodbye !!!")




os._exit(1)



# tpe().__name__