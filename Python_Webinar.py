who = ['Ethan', 'Minh', 'Dang'] #declare a list of names
random = 'abcdxyz'

pairs = [ (a,b) for a in range (4)
                for b in range (4) if a != b]
#function to make a rotation
def generator (n):
    for i in range (n):
        yield 1 + i

#function to add ages
def age (E, M, D):
    sum = E + M + D
    return sum

#Total age
total = age (16, 16, 17)

it = generator (3)

 #for loop to repeatedly print out names
for i in it: 
    for w in who:
        print ('Hey ' + w)
        print (random [1:3])
        print (pairs)
        
print ("Their total age is ", total )  
