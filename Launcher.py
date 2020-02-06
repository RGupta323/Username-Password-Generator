import random
#File to generate a random username or password 

#function to generate a username 
#inputs: length=the length of the username, hasLetters= boolean value to indicate if a username has letters, hasNumbers=boolean value 
#to indicate if it has numbers, hasSpecialChar=boolean value that indicates if there is any special characters
def genUsername(length, hasLetters, hasNumbers, hasSpecialChar, letters, numbers, specialChar): 
    return generate(length, hasLetters, hasNumbers, hasSpecialChar); 



def generate(length, hasLetters, hasNumbers, hasSpecialChar, letters="abcdefghijklmnopqrstuvwxyz"+"abcdefghijklmnopqrstuvwxyz".upper(),
numbers="0123456789", specialChar="""~`!@#$%^&*()_-+={}[]\|;:'",.<>?/-*/"""): 
    username=str()
    for i in range(length): 
        r=random.randint(0,2); 
        if(r==0 and hasLetters): 
            username+=letters[random.randint(0,len(letters)-1)]; 
        
        if(r==1 and hasNumbers): 
            username+=numbers[random.randint(0,len(numbers)-1)]
        
        if(r==2 and hasSpecialChar): 
            username+=specialChar[random.randint(0,len(specialChar)-1)]
    return username; 

    #function to generate a random password 
    def genPassword(length,hasLetters, hasNumbers, hasSpecialChar): 
        return generate(length, hasLetters, hasNumbers, hasSpecialChar); 

#print(genUsername(8,True, True, False)) 