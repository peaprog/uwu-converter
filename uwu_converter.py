#epic owo converting thingy to make them memes

normal_text = input("enter text to be uwufied: ")

char_list = ["a", "u" ,"o"]


matched_list = [characters in char_list for characters in normal_text]
print(matched_list)

Boolean in matched_list for o in normal_text:
    if o == True:
        UwU = normal_text.replace("o","Owo")
        print(UwU)


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
    return translate
