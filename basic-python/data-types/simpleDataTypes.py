text = "This is a text"
int = 23
double = 23.5
boolean = True

# exaples using data strings

name = "Juan"
lastName = "Vidal"
fullName = name + " " + lastName
concatenatedFullName = f"{name} {lastName}" # this converts everything into a string data

# membership operators -- both returns a boolen value
print('u' in concatenatedFullName) # verifing if there is a character or characters into a string
print('u' not in concatenatedFullName) # verifing if there isn't a character or characters into a string