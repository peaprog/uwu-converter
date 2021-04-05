print("""-------------------------------------------
Welcome to uwu converter!
""")
normal = input("Please enter text to be UWUfied: ")


def uwu_converter(phrase):
    translation = ""
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


uwu_converter(normal)
