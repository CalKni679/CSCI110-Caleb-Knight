#----------------------------|
#Caleb Knight                |
#CSCI110                     |
#Number 5 in Section 8.19    |
#----------------------------|


import string

#Para= My whole list of words from the movie quote
#Word_Count= My total word count



paragraph = """ For my ally is the Force, and a powerful ally it is. Life creates it, makes it grow. 
Its energy surrounds us and binds us. Luminous beings are we, not this crude matter. 
You must feel the Force around you; here, between you, me, the tree, the rock, everywhere, yes. 
Even between the land and the ship. """


def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct

para = remove_punctuation(paragraph).split()
print(para)


word_count = len(para)

def count_e(para):
    count = 0
    for word in para:
        if "e" in word:
            count += 1
    return(count)


e_in_words = count_e(para)
    
final_word_percent = (e_in_words / word_count)*100
print("Your awesome Star Wars moment contains {0} words, of which {1} ({2}%) contain an e."
      .format(word_count, e_in_words, final_word_percent))

