import pandas as pd

data = pd.read_csv("nato_code.csv")
#p_letters = data.set_index('letter')['code'].to_dict()
p_letters = {row.letter: row.code for index,row in data.iterrows()}

while True:
    try:
        word = input("write a word: ")
        phoenic_list = [p_letters[letter.upper()] for letter in word]
        print(phoenic_list)
    except KeyError:
        print("Sorry only letters allowed")