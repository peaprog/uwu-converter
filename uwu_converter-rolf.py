print("""-------------------------------------------
Welcome to uwu converter!
""")
normal = input("Please enter text to be UWUfied: ")


def uwu_converter(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "Owo"
            else:
                translation = translation + "owo"
        else:
            translation = translation + letter
    print(translation)


uwu_converter(normal)
