#------------------------|
#Caleb Knight            |
#CSCI110                 |
#Number 9 in section 7.26|
#------------------------|


#A triangular number counts objects arranged in an equilateral triangle#

def print_triangular_numbers(n):
    total = 0 
    for triangle in range (1, n):
        total = total + triangle
        print (triangle, "\t", total)
    
   
  
  
    
print_triangular_numbers(6)