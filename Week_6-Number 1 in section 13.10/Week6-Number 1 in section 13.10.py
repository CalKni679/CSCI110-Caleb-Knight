#--------------------------|
#Caleb Knight              |
#CSCI110                   |
#Number 1 in section 13.10 |
#--------------------------|


#Modified from section 13.7
def reverse(oldfile, newfile):
    infile = open(oldfile, "r")
    outfile = open(newfile, "w")
#Modified from section 13.4
    text = infile.readlines()    
    text.reverse()
    for v in text:
        outfile.write(v + "\n")

#End of section 13.7
    infile.close()
    outfile.close()

reverse("friends", "output")

 