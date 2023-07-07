# Game is set in a funfair. Player gives their tickets to enter
def game_start():
 while True:
      print('"Tickets please... Tickets.. Hi, thank you..Oh! Hello, you must be new!\n Welcome to Merrymeadows funfair. My name is Lucy. What is your name?"\n')
      name = input('Please Enter your name:\n ')
      print('"Hi,' + name ,'"')
      location = input('Where would you like to go first? The lace market, Merry-go-round, or the farm shop? \n')
      print('"Great! Lets go!"\n')
      print('Heading to ' + location)
      break 
      walk()

def walk():
 print('...\n')
 print('"STOP! DO NOT GO ANY FURTHER"\n "Sorry, we are now closing...\n')
 first_location()

def first_location():
  print('Amidst the radiant sunbeams that bathed the vibrant medieval fairgrounds of MerryMeadow, the joyful atmosphere of the fair seemed unbreakable.\nColorful pennants fluttered merrily in the breeze, mingling with the tantalizing aroma of caramelized apples and freshly spun cotton candy.\n Laughter and music filled the air, and chatter echoed across the bustling fair. But hidden beneath the facade of delight, a dark shadow had cast its spell over the festivities.\n Lady Amara, beloved by all the folk of Merrymeadow, had been discovered dead within her regal tent, her crown askew and a haunting mystery in the air.')
  print('Are you ready to uncover the truth of Merrymeadow?\n')
  answer = str(input('Please answer yes or no: \n'))

  if answer = "yes" or "Yes" : 
  print('Lady Amara was discovered by her daughter in law Clara.\n Go find Clara?')
       find = str(input())
       if find = "yes" or "Yes"
       findclara()

  elif answer = "no" or "No" : 
  print('Not up for the challenge?... heading back home.')
  print("Type head back to town to try again.\n")
      restart = str(input())
       if restart = "head back to town" or "Head back"
       main()
       
  except : ValueError :
  print("Sorry I didn't catch that...")
  break

def main():
     game_start()
     walk()
     first_location()

main()