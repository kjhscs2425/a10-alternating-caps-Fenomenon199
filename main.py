#phrase you want to change


# define 
def teddy(song):
    new_string=""
    even= True 
    for character in song : 
        if even: 
            new_string += character.upper()
        else:
            new_string+= character 
        even= not even 
    return new_string  


# call 
print(teddy(" hold me close") )



