def main ():
  while (ValueError):
    try:
        x = int(input ('Starting Code Challenge '))
        count = 0
        if 0 <= x <= 9:
          print ('Starting while loop - counting to 10')
          while (count <= 9):
            print (count)
            count += 1
            if x == count:
              print ('The user\'s variable is equal to the count variable')
              print ("Count = ", count)
              print ("User = ", x)
              continue
          print ('End the counting program')
        else:
          print ('Type in a number between 0 and 9')
    except ValueError:
      print ('Type in something valid')
    
main ()
