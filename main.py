
#Using default Python Functions:
with open("morse.csv") as morse_raw:
     morse_list= morse_raw.read().split("\n")
     letters = [letter.split(",")[0] for letter in morse_list if not letter.split(",")[0] == "letter"]
     code  = [letter.split(",")[1] for letter in morse_list if not letter.split(",")[0] == "letter"]


string_to_translate = input("Enter the string to convert to morse code: ").upper()

translated_list= []
translated_word = ""


for letter in string_to_translate:

     letter_index = letters.index(letter)

     morse_letter = code[letter_index]

     translated_list.append(morse_letter+" ")

translated_word = translated_word.join(translated_list)

print(translated_word)