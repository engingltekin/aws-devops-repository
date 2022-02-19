'''
Write a Python Program using text files  "C://Users//Engin-Didem//OneDrive//Desktop//phonebook.txt"
to create and maintain a Phone Book.
The Phone Book will display the
following Menu and will support
the corresponding functionality

*** Phone Book Menu ***
Welcome to the phonebook application
1. Find phone number
2. Insert a phone number
3. Delete a person from the phonebook
4. Terminate
Select operation on Phonebook App (1/2/3) :
**********************
'''
import re

phone_match = re.compile("^(\w{3}-\w{3}-\w{4})$")#basic regex

class PhoneInfo:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

phoneList = []


def show_main_menu():
    ''' Show main menu for Phone Book Program '''
    print("\n   Welcome to the phonebook application\n"+
            "1. Find phone number\n"+
            "2. Insert a phone number\n"+
            "3. Delete a person from the phonebook\n"+
            "4. Terminate\n")
    choice = input("Select operation on Phonebook App (1/2/3) : ")
    try:
        match choice:
            case "1":
                #Check if the Phone book is Empty
                #else find record from list and display phone number and information
                if not phoneList:
                    print("Phone Book is empty")
                else:
                #Find
                    search_contact_record()
                ent = input("Press Enter to continue ...")
                show_main_menu()
            #return to home menu after each operation is completed
            case "2":
                #create contact record
                enter_contact_record()
                ent = input("Press Enter to continue ...")
                show_main_menu()
            case "3":
                #search and delete phone record
                delete_contact_record()
                ent = input("Press Enter to continue ...")
                show_main_menu() 
            case "4":
                print ('Exiting Program')        
            case _:
                print("Invalid number, Please Enter [1 to 4]\n")
                ent = input("Press Enter to go back to main menu ...")
                show_main_menu()  
    except:
        print("An error has occurred!") 
        ent = input("Press Enter to continue ...")
        show_main_menu() 
    #finally: For any clean up 
                
    
def search_contact_record():
    ''' This function is used to searches a specific contact record '''
    search_name = input("Enter First name for Searching contact record: ")
    search_name = search_name.title()
    found = False   
    for phoneInfo in phoneList:
        if search_name == phoneInfo.name:
            print('Name : {}, Phone Number : {}'.format(phoneInfo.name,phoneInfo.phoneNumber))
            found=True
            break
    if  found == False:
        print("There's no contact Record in Phone Book with name = " + search_name )

def enter_contact_record():
    ''' It  collects contact info name and phone '''
   
    personName = input('Insert name of the person: ')
    personName = personName.title()
    phone = input('Please enter a phone number in the format XXX-XXX-XXXX: ')
    while not phone_match.match(phone):
        phone = input('Invalid Phone number! Please enter a phone number in the format XXX-XXX-XXXX: ')

    if not phoneList:
        phoneList.append(PhoneInfo(personName, phone))
        print( "This contact\n " + personName + " has been added successfully!")
    else:
        for phoneInfo in phoneList:
            if personName == phoneInfo.name and phone == phoneInfo.phoneNumber:    
                print('Contact already exist!')
            else:
                phoneList.append(PhoneInfo(personName, phone))
                print( "This contact\n " + personName + " has been added successfully!")

def delete_contact_record():
    personName = input('Insert name of the person delete: ')
    personName = personName.title()
    for phoneInfo in phoneList:
        if personName == phoneInfo.name:
            phoneList.remove(phoneInfo)


          

#Initiate the program
show_main_menu()