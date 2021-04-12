print("""-------------------------------------------
    Welcome to uwu converter!
    """)


def uwu_converter():
    translation = ""
    
    phrase = input("\nPlease enter text to be UWUfied: ")

    for letter in phrase:
        if letter.lower() in "aeio":
            if letter.isupper():
                translation = translation + "Owo"
            else:
                translation = translation + "owo"
        elif letter.lower() in "u":
            if letter.isupper():
                translation = translation + "Uwu"
            else:
                translation = translation + "uwu"
        else:
            translation = translation + letter
            
    print(translation)
    return(phrase)


while True:
    uwu_converter()
    answer = input("\n-------------------------------------------\nContinue? (y/n): ")
    if answer.lower() == 'n':
        break
