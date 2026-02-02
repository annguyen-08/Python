def main ():
  x = True
  while x:
    try:
        user = int(input ('Enter a number bigger than 20: '))
        count = 0
        if user > 20:
          print ('Starting while loop - Print Count Variable')
          print ('The user\'s input started as ', user)
          while (user > 1):
            user = user / 2
            count += 1
            print ("The current value of the user input after some math is ", user)
            print ("The while loop has looped ", count, " time")
          print ('Ending While Loop')
          print ("The While Loop, looped a total of ", count, " times")
          x = False
        else:
          print ('Type in a number bigger than 20')
    except ValueError:
      print ('Type in something valid')
main ()
