#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX_______START_______XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
from itertools import permutations 
import string
import os

##-------------------------Adding keywords Start----------------------------------------------------
def keyinput():	
	total_info = input('Enter the keywords each with one space gap if done press ENTER: ')
	list_info = total_info.rsplit (" ")
	commonps = open("commonps_add.txt", "r")
	read_commonps = str(commonps.read()).rsplit("\n")
	commonpass = open("common_passwords.txt", "r")
	read_commonpass = str(commonpass.read()).rsplit("\n")
	for i0 in read_commonpass:
		commonpass = i0 + "\n"
		g.write(commonpass)
	for i1 in read_commonps:
	    for j1 in list_info:
	        normal_list_info = j1 + "\n"
	        commonps = i1 + "\n"
	        pre = i1 + j1 + "\n"
	        suf = j1 + i1 + "\n" 
	        g.write(normal_list_info)
	        g.write(commonps)
	        g.write(pre)
	        g.write(suf)
##-------------------------Adding keywords End---------------------------------------------------

##-------------------------file START---------------------------------------------------
file_name=input('Enter name of the file to save all the passwords(and usernames if selected) : ')
y3=input('Do you want to save files in costume location(if not its will be in default)//(y/n):')
if y3=="y" or y3 =="Y":
        loc=input('Enter the location of the file to save(EX:c:/directory/path/you/want/): ')
        fname=loc + file_name +'_password'+ '.txt'
        uname=loc+file_name +'_user'+ '.txt'
else:        
        fname=file_name +'_password'+ '.txt'
        uname=file_name +'_user'+ '.txt'
g = open (fname, "a")


##-------------------------file END---------------------------------------------------


##--------------------------------Jumbling Start--------------------------------------------------------------------------------
def jumbled():
	for i2 in list_info:
		jinput = i2
		asci = string.ascii_letters 
		permutate = permutations(jinput) 
		dictionary = [] 
		for i3 in list(permutate): 
		    # Print only if not in dictionary 
		    if (i3 not in dictionary): 
		        dictionary.append(i3) 
		        jumbled=''.join(i3)
##		        print(jumbled)
		        p = jumbled + "\n"
		        g.write(p)
##--------------------------------Jumbling End--------------------------------------------------------------------------------

##-------------------------Merging 2 keywords Sart----------------------------------------------------
def merge():
	for i3 in list_info:
	    for j3 in list_info:
	        k3 = i3 + j3 + "\n" 
	        l3 = j3 + i3 + "\n" 
	        g.write(k3)
	        g.write(l3)
##-------------------------Merging 2 keywords End----------------------------------------------------


##-----------------------------USER START--------------------------------------------------------
def username():
	g1 = open (uname, "a")
	Usernames = input("Enter the usernames each with one space gap if done press ENTER: ")
	User=Usernames.rsplit(" ")
	
	for i4 in User:
		k4=i4 + "\n"
		g1.write(k4)
	print("Generating usernames done!")

##-----------------------------USER START--------------------------------------------------------


y0=input("Do you want to enter usernames? : ")
if y0=="y" or y0 =="Y":
	username()

keyinput()

y1=input("Do you want to jumble each letter of each keyword?(y/n) : ")
if y1=="y" or y1 =="Y": 
	jumbled()
	print('Jumbling completed in all possible combinations for each word')

y2=input("Do you want merge every keyword with other keywords?(y/n) : ")
if y2=="y" or y2 =="Y":
	merge()
	print('merging completed in all possible combinations for each word')

print('Done check in the location')##DONE
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX_______END_______XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
