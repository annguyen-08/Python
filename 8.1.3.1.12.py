def language():
    #language = input("Which language do you prefer? English, Spanish, France, Vietnamese, Chinese?")
    x = True
    while x:
      language = input("Which language do you prefer? English, Spanish, France, Vietnamese, Chinese?")
      if language == "English":
        greet = "Hello"
        return greet
      elif language == "Spanish":
        greet = "Hola"
        return greet
      elif language == "France":
        greet = "Bonjour"
        return greet
      elif language == "Vietnamese":
        greet = "Xin Chao"
        return greet
      elif language == "Chinese":
        greet = 'Ni hao'
        return greet
      else:
        print ("Please only choose one of the available language")
        greet = "Wrong"
      if greet != "Wrong":
        x = False
        
def challenge_3():
  name = input("What's your name?")
  print (language(), name.capitalize())

def main():
  challenge_3()

main ()
