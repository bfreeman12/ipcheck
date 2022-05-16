import csv


def search_ip():
     with open ('ipaddr.csv','r') as file:
         #replace 'ipaddr.csv' name of csv file
         myfile = csv.reader(file)
         search_value = input("please enter the ip address: ")
         for row in file:
             if search_value in row:
                 print(row)
                 break
             else:
               print("Entry not found please add it: ")
               add_ip()
               break
#search_ip function opens selected csv file and reads it, then based on user input searches the file


def add_ip():
    with open ('ipaddr.csv','a') as file:
        #replace 'ipaddr.csv' name of csv file
        myfile = csv.writer(file)
        num_of_ip = int(input("enter the number of ip addresses you would like to add: "))
        for i in range (num_of_ip):
         ip = input("please enter the ip address: ")
         company = input("please enter the company or organization: ")
         country = input("please enter the country it is registered in: ")
         myfile.writerow([ip,company,country])
         break
#add_ip function does what it says. opens the file, and based on user input adds a row to the csv file

#below is the actual program itself, based on user input will run the specified function



print("""
***notice***
if trying to read from a csv file 
make sure the script and file are
in the same directory =)

""")


program_choice = input("""please enter the value of what you're trying to do:
1: search for known ip addresses
2: add a new ip address to the list
value: """)
program_choice = int(program_choice)
if program_choice == 1 :
    search_ip()
    continue_value = input("would you like to search again? ('yes' or 'no') ")
    while continue_value == "yes":
        search_ip()
        continue_value = input("would you like to search again? ('yes' or 'no') ")
    else:
        quit
elif  program_choice == 2 :
    add_ip()
else : 
    print("error")



#
#
#
#using this to develop my python skills 
#intent is to eventually create a search engine that we in the shop can use to whitelist known good ip addresses
#and hopefully gather a list of malicious or just ip addressess we would like to block and have easy access to all
#this information
#
#
#