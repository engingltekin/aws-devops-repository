

from asyncio.windows_events import NULL

#receive user input
givenNumber = input("Please provide miliseconds:")

#check if given value is a number
if givenNumber.isdigit()==False:
    print("Not Valid Input !!!")
    quit()

 #than conver to an integer to process further
givenNumber = int(givenNumber)  

#if given number is negative
if givenNumber < 0:
    print("Not Valid Input !!!")
    quit()

if givenNumber < 1000:
    print(f'{givenNumber} millisecond/s')    
    quit()
else:
    result = ""
    if givenNumber>3600000:
        hours = int(givenNumber/3600000)
        if hours>24:
            print("Hours are greater than a day!!!")
            quit()
        remainderseconds = int(givenNumber%3600000)
        result+=f"{str(hours)} hour/s "
        if remainderseconds>60000:
            minutes = int(remainderseconds/(60000))
            remainderminutes = int(remainderseconds%60000)
            result+=f"{str(minutes)} minute/s "
            if remainderminutes>1000:
                seconds = int(remainderminutes/1000)
                result+=f"{str(seconds)} second/s "
        print(result)   
        quit()
    elif givenNumber>60000:
            minutes = int(givenNumber/(60000))
            remainderminutes = int(givenNumber%60000)
            result+=f"{str(minutes)} minute/s "
            if remainderminutes>1000:
                seconds = int(remainderminutes/1000)
                result+=f"{str(seconds)} second/s"
            print(result)   
            quit()        
    else: 
        print(f'{givenNumber/1000} second/s')     
        quit()