# Game is set in a funfair. Player gives their tickets to enter. 
# There are three suspects in this game
suspects = []
weapons = []

def game_start():
      print('"Tickets please... Tickets.. Hi, thank you..Oh! Hello, you must be new!\n Welcome to Merrymeadows funfair. My name is Lucy. What is your name?"\n')
      name = input('Please Enter your name:\n ')
      print('"Hi,' + name.title(),'"')
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
     print('Amidst the radiant sunbeams that bathed the vibrant medieval fairgrounds of MerryMeadow, the joyful atmosphere of the fair seemed unbreakable.\nColorful pennants fluttered merrily in the breeze, mingling with the tantalizing aroma of caramelized apples and freshly spun cotton candy. Laughter and music filled the air, and chatter echoed across the bustling fair. But hidden beneath the facade of delight, a dark shadow had cast its spell over the festivities. Lady Amara, beloved by all the folk of Merrymeadow, had been discovered dead within her regal tent, her crown askew and a haunting mystery in the air.')
     print('Are you ready to uncover the truth of Merrymeadow?...\n')
     print('Lady Amara was discovered by her daughter in law Clara.\n', '"Hmmm, I wonder if Clara knows anything."')
     accept = input('Find Clara?')
     while True: 
          accept = input('Find Clara? Y/N')

          if accept.lower().strip() != "y" and accept.lower().strip() != "n":
               print("Sorry, I didn't quit catch that...Please try again\n")
               continue 
          else : 
               break

     if accept.lower().strip() == "y":
          find_clara()
     elif accept.lower().strip() == "n":
          print('Not up for the challenge?... heading back home.')
          print('"Hmm, I probably should speak to Clara..."')
          find_clara()
    
def find_clara():
# Daughter of Lady Amara, spolit and just got her inheritence. She claims to have spoken to the major at the fun fair. 
     print("'Heading to Clara's house...")
     print("Hmm, Shall I ask Clara where she was or shall I ask who she was with when her mother died?")
     question_answer = input('where or who?')
     #Bite video tutorial used to help write while loops
     while True: 
          question_answer = input('where or who?')
          if question_answer.lower().strip() != "where" and question_answer.lower().strip() != "who":
               print("Sorry, I didn't quit catch that...Please try again\n")
               continue 
          else : 
               break

     if question_answer.lower().strip() == "where":
          print('"Well Obviously I was at the funfair... like the rest of the town silly! I was going to meet my mother... she said I can go on all the rides with her and use up my allowence. The sad thing is I now have no mother and a huge allowence."')
          print("Hmm, someone must have seen her.")
          print('"Did anyone see you Clara?"')
          print('"I did say hi to the major, but he was probably too busy to see me."')
          print("Adding Clara to list of suspects...")
          suspects.append("Clara")
          print("Going to find the major...")
     elif question_answer.lower().strip() == "who":
          print('"I did say hi to the major, but he was probably too busy to see me."')
          print("Adding Clara to list of suspects...")
          suspects.append("Clara")
          print("Going to find the major...")
     
def find_the_major():
print("'Heading to The Major's house...")
     print('"Oh Hi! I dont think I was expecting company... erm do come in."')
     print('"How well did I know Lady Amara? Well, we worked together. Strickly professional."')
     thought = input("Do you want to ask where he was the day Lady Amara died? Y/N?\n")
     #Bite video tutorial used to help write while loops
     while True: 
          question_answer = input("Do you want to ask where he was the day Lady Amara died? Y/N?")
          if question_answer.lower().strip() != "y" and question_answer.lower().strip() != "n":
               print("Sorry, I didn't quit catch that...Please try again\n")
               continue 
          else : 
               break

     if question_answer.lower().strip() == "y":
          print('Ha! I was at the funfair... and she was fine when I saw her... I mean... The day before, we ran though the finaces!')
          secound_thought = input("Ask another question? Y/N")
           while True: 
          secound_thought = input("Ask another question? Y/N")
          if secound_thought.lower().strip() != "y" and secound_thought.lower().strip() != "n":
               print("Sorry, I didn't quit catch that...Please try again\n")
               continue 
          else : 
               break
          if secound_thought.lower().strip() == "y":
               print('"Sir, when was the last time you saw Lady Amara?"')
               print('"Alright! Fine! I was with her that morning... were having an affiar, but we had ended it. She was going to tell her husband! Count Chrispin is my friend you see... And when he saw us.\n Oh, I have shared to much. Please do not say a word! My reputation is on the line."')
               print("Adding the Major to list of suspects...")
               suspects.append("The Major")
               print('I think I need to pay her husband a visit..')
               print("Going to find Count Chrispin...")
     elif secound_thought.lower().strip() == "n":
          print('"I do not want to cause any drama, but you should probably talk to her husband. He was pretty angry after finding out Lady Amara and I...."', '"Nevermind! Ignore me!"')
          print("That was odd... Adding The Major to list of suspects...")
          suspects.append("The major")
          print("Going to find Count Chrispin...")

# def find_Count_Crispin():

def main():
     game_start()
     walk()
     first_location()
     find_clara()
     find_the_major()
     find_count_crispin()

main()