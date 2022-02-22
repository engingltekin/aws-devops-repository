'''
Write a Python Program using text files
to create and maintain a Phone Book.
The Phone Book will display the
following Menu and will support
the corresponding functionality

*** Phone Book Menu ***
Enter 1,2,3 or 4:
Enter 1 To Display Your Contacts Records
Enter 2 To Add a New Contact Record a new contact
Enter 3 To search your contacts
Enter 4 To Quit
**********************

author: www.Easycodebook.com (c)
'''
file_name = "C://Users//Engin-Didem//OneDrive//Desktop//phonebook.txt"
file1 = open(file_name, "a+")
file1.close


def show_main_menu():
    ''' Show main menu for Phone Book Program '''
    print("\n   *** Phone Book Menu ***\n"+
          "author: www.Easycodebook.com (c)\n"+
          "------------------------------------------\n"+
          "Enter 1,2,3 or 4:\n"+
          "Enter 1 To Display Your Contacts Records\n" +
          "Enter 2 To Add a New Contact Record\n"+
          "Enter 3 To Search your contacts\n"+
          "Enter 4 To Quit\n**********************")
    choice = input("Enter your choice: ")
    if choice == "1":
        file1 = open(file_name, "r+")
        file_contents = file1.read()
        if len(file_contents) == 0:
            print("Phone Book is empty")
        else:
            print (file_contents)
        file1.close
        ent = input("Press Enter to continue ...")
        show_main_menu()
    elif choice == "2":
        enter_contact_record()
        ent = input("Press Enter to continue ...")
        show_main_menu()
    elif choice == "3":
        search_contact_record()
        ent = input("Press Enter to continue ...")
        show_main_menu()
    elif choice== "4":
        print("Thanks for using Phone Book Program presented by:"+
              "\nwww.EasyCodeBook.com "+"\nFor Perfect Programming Tutorials: Python, Java, C, C++")
    else:
        print("Wrong choice, Please Enter [1 to 4]\n")
        ent = input("Press Enter to continue ...")
        show_main_menu()
        
def search_contact_record():
    ''' This function is used to searches a specific contact record '''
    search_name = input("Enter First name for Searching contact record: ")

    search_name = search_name.title()
    file1 = open(file_name, "r+")
    file_contents = file1.readlines()
     
    found = False   
    for line in file_contents:
        if search_name in line:
            print("Your Required Contact Record is:", end=" ")
            print (line)
            found=True
            break
    if  found == False:
        print("There's no contact Record in Phone Book with name = " + search_name )

def enter_contact_record():
    ''' It  collects contact info firstname, last name, email and phone '''
   
    first = input('Enter First Name: ')
    first = first.title()
    last = input('Enter Last Name: ')
    last = last.title()
    phone = input('Enter Phone number: ')
    email = input('Enter E-mail: ')
    contact = ("[" + first + " " + last + ", " + phone + ", " + email +  "]\n")
    file1 = open(file_name, "a")
    file1.write(contact)
    print( "This contact\n " + contact + "has been added successfully!")

show_main_menu()