from Launcher import * 
from Database import * 
import sys 

#HERE'S A BUNCH OF HELPER FUNCTIONS BECAUSE APPARENTLY PYTHON CAN'T READ!!!!!
#function to identify a set 
def isSet(aString): 
    return (aString[0]=="-" and aString[1]=="{" and aString[-1]=="}")



#boolean functions to determine is a particular string has letters, numbers or symbols. 
#In this way we can determine when judge() returns false for any key if that false is value is indeed a set or the user 
#didn't put it there, so for example gen username -numbers -symbols and gen username -{abcdefghijklmnopqrstuvwxyz} -numbers -symbols
#are different commands. 
def isLetters(alist): 
    #return (("-letters" in alist[i]) or (isSet(alist[i])) or alist[i].isalpha())
    return (any(["-letters" in element or isSet(element) or element.isalpha() for element in alist]))

def isNumbers(alist): 
    #return (("-numbers" in alist[i]) or (isSet(alist[i]))); 
    return (any(["-numbers" in element or isSet(element) or element.isdigit() for element in alist]))

def isSymbols(alist): 
    #return (("-symbols" in alist[i]) or (isSet(alist[i]))); 
    return (any(["-symbols" in element or isSet(element) or (not element.isalpha() and not element.isdigit()) for element in alist]))

#function to take into a list and return a tuple indicating how many stuff is there: -letters -numbers -symbols the tuple would be (3,0)
#but if there are sets then that number would be counted as well so: gen username -letters -numbers -{!@#$} the function would return 
#(2,1); 
#very important here, this function gives you a list based on numbers, so you know how many of what kind either -### or a set 
#now we can modify this function to determine what exactly do we have so instead of [3,0], we can have [1,1,1,0,0,0], a sort of binary
def judge(aString,arg): 
    """Original Judge function
    lis=[0,0]
    lis[0]=("-letters" in aString)+("-numbers" in aString)+("-symbols" in aString); 
    lis[1]=sum([isSet(element) for element in arg])
    return lis; """
    #now going to be modified so that it's a longer list which has a length of 6. 
    lis=list(); 
    d={}
    """lis.append("-letters" in aString)
    lis.append("-numbers" in aString); 
    lis.append("-symbols" in aString); """ 
    d["letters"]="-letters" in aString; 
    d["numbers"]="-numbers" in aString; 
    d["symbols"]="-symbols" in aString; 
    return d; 
#User Interface - this is going to be a terminal based command system. 
#Program will always be running, better way to test functions

#Functions here...
# 
# List of commands that the program uses 
def help(): 
    a="""The following list of commands is below: 
        IMPORTANT NOTE: ALL COMMANDS IF BEING EXECUTED THROUGH WINDOWS MUST HAVE: python C:/..../Main.py "gen username ...." 
        THIS IS EXTREMELY IMPORTANT. 
        THE WINDOWS POWERSHELL MUST BE EXECUTED FROM THE DIRECTORY IN WHICH PYTHON IS DOWNLOADED THEN TYPE: python 
        AFTER PYTHON YOU INPUT THE FILE IN WHICH MAIN.py OF THIS PROJECT IS STORED 
        THEN AS A STRING INPUT THE TERMINAL BASED COMMAND 

        Generate Username: 
            To generate a random username with letters(a-z,A-Z), numbers(0-9), and symbols: gen username 
            to generate a random username with no letters: gen username -numbers -symbols 
            To generate a random username with a set of specific letters gen username -{abc} -numbers -symbols 
            To generate a random username with only upper case letters: gen username -upper -numbers -symbols 
            To generate a random username with only lower case letters: gen username -lower -numbers -symbols
            To generate a random username with a specific set of symbols: gen username -letters -numbers -{!@#$%^}
            To generate a random username with a specific set of numbers: gen uesrname -letter -{1234} -symbols 
            Can also generate a random username with multiple specific sets: gen username -{abcdef} -{123} -{!@#$%^}
        
        Generate Password: 
            To generate a random password with letters(a-z,A-Z), numbers(0-9), and symbols: gen password 
            to generate a random password with no letters: gen password -numbers -symbols 
            To generate a random password with a set of specific letters gen password -{abc} -numbers -symbols 
            To generate a random password with only upper case letters: gen password -upper -numbers -symbols 
            To generate a random password with only lower case letters: gen password -lower -numbers -symbols
            To generate a random password with a specific set of symbols: gen password -letters -numbers -{!@#$%^}
            To generate a random password with a specific set of numbers: gen password -letter -{1234} -symbols 
            Can also generate a random password with multiple specific sets: gen password -{abcdef} -{123} -{!@#$%^}
        
        After a username AND password is generated, you will be prompted to enter the website, and once that occurs that all the 
        info of the entry will be stored into a database... 

        Search
            To search for a username: search -[username]
            To search for a password: search -[password]
            To search for a username based on a set: search -[username] on {abc}
            To search for password based on a set: serach -[password] on {###}

        Delete
            To delete an entry: delete -[username] -[password] 
                -Note: Because all usernames and passwords are all unique, you won't need to enter in a website
        
        Help
            To make this long message appear again, type: -help 
    
    """
    return a; 

#Main Script here.... 
print(help()); 
arg=sys.argv; #this is going to be a list
#print(arg); #debugging
userInput=" ".join([arg[element] for element in range(1,len(arg))])
arg=[arg[i] for i in range(1,len(arg))]
print(arg);
arg=arg[0].split(" ");  
print(userInput); 
 
userInput=" ".join([arg[i] for i in range(1,len(arg))])
print(userInput); 

#here are going to be the various if statements to cipher the commands and re-direct them to the proper if statement... 

if(arg[0]=="gen" and arg[1]=="username"): 
    arg=[arg[i] for i in range(2,len(arg))]
    print("line 107: "+str(arg)); 
    astr=" ".join([element for element in arg])
    nums=judge(astr,arg); 
    print("line 71: "+str(nums));
    #okay so nums is now alist of [True, True, True]
    #note that the list is of the format [letters, numbers, symbols]
    #IF nums[0]==False, THEN numbers is a defined set... 
    letters, numbers, symbols = list(), list(), list(); 
    areLetters, areNumbers, areSymbols=False, False, False; 
    """if(not nums["letters"]): 
        #defined set of letters 
        letters=arg[0]; 
    if(not nums["numbers"]): 
        numbers=arg[1]; 
    if(not nums["symbols"]): 
        symbols=arg[2]; """
    
    length=random.randint(8,10); #will be randomly generated for now... user will enter in the length though... 
    #Now another thing you have to determine if there are letters, numbers, and symbols... 
    print(isNumbers(arg)); 
    print(genUsername(length, isLetters(arg), isNumbers(arg), isSymbols(arg), letters, numbers, symbols)); 







