#-----------------------------|
#Caleb Knight                 | 
#CSCI110                      |
#Problem 3 in section 20.8    |
#-----------------------------|

infile = open("alice_words.txt", "r")
#Dictionary
alice_words = {}
#Dictionary

#Chapter 8 string cleaner
punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

def remove_punctuation(word):
    s_sans_punct = ""
    for letter in word:
        if letter not in punctuation:
            s_sans_punct += letter
    return s_sans_punct
#Chapter 8 string cleaner

for lines in infile:
    words = lines.split()

#Modified from 20.6. Counting letters
    for word in words:
     word = word.lower()
     word = remove_punctuation(word)

     alice_words[word] = alice_words.get(word, 0) + 1

#Modified from 20.2. Dictionary methods
alice_word_list = list(alice_words.keys())

alice_word_list.sort()

outfile = open("alice_words_done.txt", "w")

for w in alice_word_list:
   outfile.write(w + " " + str(alice_words[w]) + "\n")

outfile.close()