#------------------------|
#Caleb Knight            |
#CSCI110                 |
#Number 7 in Section 6.9 |
#------------------------|

import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} IT'S GOOD.".format(linenum)
    else:
        msg = ("Test at line {0} NOPE.".format(linenum))
    print(msg)


def to_secs(hour, minute, second):
    time = (hour*3600) + (minute*60) + (second)

    return time

#Provided from textbook
test(to_secs(2, 30, 10) == 9010)
test(to_secs(2, 0, 0) == 7200)
test(to_secs(0, 2, 0) == 120)
test(to_secs(0, 0, 41) == 41)
test(to_secs(0, -10, 10) == -590)





