#----------------------------|
#Caleb Knight                |
#CSCI110                     |
#Number 10 in Section 11.22  |
#----------------------------|
import sys
#Brought over from number 7 in section 6.9
def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} IT'S GOOD.".format(linenum)
    else:
        msg = ("Test at line {0} NOPE.".format(linenum))
    print(msg)
##Brought over from number 7 in section 6.9


#Write a function replace(s, old, new) 
def replace(s, old, new):
    wds = s.split(old)
    glue = new
    x = glue.join(wds)
    return x
    



#Tests
test(replace("Mississippi", "i", "I") == "MIssIssIppI")

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
test(replace(s, "om", "am") ==
    "I love spam! Spam is my favorite food. Spam, spam, yum!")

test(replace(s, "o", "a") ==
    "I lave spam! Spam is my favarite faad. Spam, spam, yum!")