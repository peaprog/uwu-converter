def uwu_converter():
    translation = ""
    phrase = input("Enter text to be uwufied or owofied: ")
    for letter in phrase:
        if letter.lower() in "u":
            if letter.isupper():
                translation = translation + "Uwu"
            else:
                translation = translation + "uwu"
        elif letter.lower() in "aeio":
            if letter.isupper():
                translation = translation + "Owo"
            else:
                translation = translation + "owo"
        else:
            translation = translation + letter
    return str(translation)
while True:
    try:
        print("-----------------------------")
        print(uwu_converter())