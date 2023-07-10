# Game is set in a funfair. Player gives their tickets to enter. 
# There are three suspects in this game
suspects = ["Clara", "The Major", "Count Chrispin"]
locations = []

def game_start():
      print('"Tickets please... Tickets.. Hi, thank you..Oh! Hello, you must be new!\n Welcome to Merrymeadows funfair. My name is Lucy. What is your name?"\n')
      name = input('Please Enter your name:\n ')
      print('"Hi,' + name ,'"')
      print('Where would you like to go first?',"The Lace market, The Merry-go-round, or The farm shop")
      travel = input()   
      print('"Great! Lets go!"')
      print('Heading to ' + travel)
      walk()

def walk():
      print('...\n')
      print('"STOP! DO NOT GO ANY FURTHER"', '"Sorry, we are now closing..."')
      first_location()

def first_location():
     print =('Amidst the radiant sunbeams that bathed the vibrant medieval fairgrounds of MerryMeadow, the joyful atmosphere of the fair seemed unbreakable.\nColorful pennants fluttered merrily in the breeze, mingling with the tantalizing aroma of caramelized apples and freshly spun cotton candy. Laughter and music filled the air, and chatter echoed across the bustling fair. But hidden beneath the facade of delight, a dark shadow had cast its spell over the festivities. Lady Amara, beloved by all the folk of Merrymeadow, had been discovered dead within her regal tent, her crown askew and a haunting mystery in the air.')
     input = ('Are you ready to uncover the truth of Merrymeadow? Yes or No?')
     input = yes
     while True: 
          print('Lady Amara was discovered by her daughter in law Clara.')
          print = input('Find Clara?')
          input = yes
          while True :
               find_clara()
     else:
          print('Not up for the challenge?... heading back home.')
          input = ('Would you like to head back to town? \n')
          input = yes
          if answer == yes :
               main()
          if answer == no :
               print('Game Over.')              

# def find_clara():

# def find_the_major():

# def find_Count_Crispin():

def main():
      game_start()
      walk()
      first_location()
     # findclara()
     # find_the_major()
     # find_count_crispin()

main()