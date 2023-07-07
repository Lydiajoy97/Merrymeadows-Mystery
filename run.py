# Game is set in a funfair. Player gives their tickets to enter
def game_start():
 while True:
      print('Tickets please... Tickets.. Hi, thank you..Oh! Hello, you must be new! Welcome to Merrymeadows funfair. My name is Lucy. What is your name?')
      name = input('Please Enter your name:')
      print('Hi,' + name)
      location = input('Where would you like to go first? The food markets, Merry-go-round, or the market?')
      print('Great! Lets go!')
      print('Heading to ' + location)
      break
      first_location()

def first_location():
  print('Amidst the radiant sunbeams that bathed the vibrant medieval fairgrounds, the joyful atmosphere of Merrymeadow seemed unbreakable. Colorful pennants fluttered merrily in the breeze, mingling with the tantalizing aroma of caramelized apples and freshly spun cotton candy. Laughter and music filled the air, and chatter echoed across the bustling fair. But hidden beneath the facade of delight, a dark shadow had cast its spell over the festivities. Lady Amara, beloved by all the folk of Merrymeadow, had been discovered lifeless within her regal tent, her crown askew and a haunting mystery in the air.')
  print('Are you ready to uncover the truth of Merrymeadow?')
  Answer = input('Y or N')

def main():
     game_start()
     first_location()

main()