


def uwu_converter():
    translation = ""
    print("""-------------------------------------------
    Welcome to uwu converter!
    """)
    phrase = input("Please enter text to be UWUfied: ")
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

while True:
    try:
        uwu_converter()
    except:
        print("What are you even doing")

