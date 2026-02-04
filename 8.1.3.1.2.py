print ("Hello")
name = input ("What's is your name ")
type (name)
print ("Your name has", abs (len (name)), "characters")

names = ['Andy', 'Minh', 'Ethan', 'Dang']
#user = input ("Do you know who is the most handsome guy?")

x = True

while (x):
    try:
        user = input("Do you know who is the most handsome guy?")
        if user == 'Andy':
            print (min (names), "is the most handsome guy")
            x = False
        else:
            print ("guess again")
    except:
        print ("guess again")

