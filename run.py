# Game is set in a funfair. Player gives their tickets to enter. 
# There are three suspects in this game
suspects = []
weapons = []

# Game start and name input
def game_start():
      print('"Tickets please... Tickets.. Hi, thank you..Oh! Hello, you must be new!\n Welcome to Merrymeadows funfair. My name is Lucy. What is your name?"\n')
      name = input('Please Enter your name:\n ')
      print('"Hi,'+ name.title(),'"')
      print('Where would you like to go first?',"The Lace market, The rides, or The farm shop")
      travel = input()
      while True:
          if travel.lower().strip() != "the lace market" and travel.lower().strip() != "the rides" and travel.lower().strip() != "the farm shop":
               print("Did you spell the places correctly? Please try again.\n")
               guilty = input('Where would you like to go?...\n')
               continue 
          else : 
               break
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
     accept = input('Find Clara? Y/N\n')
     while True: 
          if accept.lower().strip() != "y" and accept.lower().strip() != "n":
               print("Sorry, I didn't quit catch that...Please try again\n")
               accept = input('Find Clara? Y/N\n')
               continue 
          else : 
               break

     if accept.lower().strip == "y":
          find_clara()
          
     if accept.lower().strip() == "n":
          print('Not up for the challenge?... heading back home.')
          print('"Hmm, I probably should speak to Clara..."')
          find_clara()

# first suspect Clara  
def find_clara():
     print("'Heading to Clara's house...")
     print("Hmm, Shall I ask Clara where she was or shall I ask who she was with when her mother died?")
     question_answer = input('where or who?')
     #Bite video tutorial used to help write while loops
     while True: 
          if question_answer.lower().strip() != "where" and question_answer.lower().strip() != "who":
               print("Sorry, I didn't quit catch that...Please try again\n")
               question_answer = input('where or who?')
               continue 
          else : 
               break

# questions for Clara
     if question_answer.lower().strip() == "where":
          print('"Well Obviously I was at the funfair... like the rest of the town silly! I was going to meet my mother... she said I can go on all the rides with her and use up my allowence. The sad thing is I now have no mother and a huge allowence."')
          print("Hmm, someone must have seen her.")
          print('"Did anyone see you Clara?"')
          print('"I did say hi to the major, but he was probably too busy to see me. He looked like he was in a rush."')
          print("Adding Clara to list of suspects...")
          suspects.append("Clara")
          print("Going to find the major...")
          find_the_major()
     elif question_answer.lower().strip() == "who":
          print('"I did say hi to the major, but he was probably too busy to see me. He looked like he was in a rush."')
          print("Adding Clara to list of suspects...")
          suspects.append("Clara")
          print("Going to find the major...")
          find_the_major()

# secound suspect the major
def find_the_major():
     print("'Heading to The Major's house...")
     print('"Oh Hi! I dont think I was expecting company... erm do come in."')
     print('"How well did I know Lady Amara? Well, we worked together. Strictly professional."')
     thought = input("Do you want to ask where he was the day Lady Amara died? Y/N?\n")
     #Bite video tutorial used to help write while loops
     while True: 
          if thought.lower().strip() != "y" and thought.lower().strip() != "n":
               print("Sorry, I didn't quit catch that...Please try again\n")
               thought = input("Do you want to ask where he was the day Lady Amara died? Y/N?\n")
               continue 
          else : 
               break

     if thought.lower().strip() == "y":
          print('"Ha! I was at the funfair... and she was fine when I saw her... I mean... The day before, we ran though the finaces!"')
          secound_thought = input("Ask another question? Y/N\n")
          while True: 
               if secound_thought.lower().strip() != "y" and secound_thought.lower().strip() != "n":
                    print("Sorry, I didn't quit catch that...Please try again\n")
                    secound_thought = input("Ask another question? Y/N\n")
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
               find_count_crispin()
          elif secound_thought.lower().strip() == "n":
               print('"I do not want to cause any drama, but you should probably talk to her husband. He was pretty angry after finding out Lady Amara and I...."', '"Nevermind! Ignore me!"')
               print("That was odd... Adding The Major to list of suspects...")
               suspects.append("The major")
               print("Going to find Count Crispin...")
               find_count_crispin()

# Third Suspect Count Crispin
def find_count_crispin():
     print('"Who is it?! I do not want company right now. Go away."')
     print('You spoke to the Major... DO NOT TALK ABOUT THAT MAN TO ME!')
     count_question = input("Question Count Crispin on his whereabouts the morning she died? Y/N\n")
     # Bite video tutorial used to help write while loops
     while True: 
          if count_question.lower().strip() != "y" and count_question.lower().strip() != "n":
               print("Sorry, I didn't quit catch that...Please try again\n")
               count_question = input("Question Count Crispin on his whereabouts the morning she died? Y/N\n")
               continue 
          else : 
               break

     if count_question.lower().strip() == "y":
          print('"I can not believe you would be this insenstive. I was with my wife. Until..."', '"Until...that man decided decided to surprise her with breakfast in the tent. That is when I found out about the affair."')
          secound = input("Ask another question? Y/N\n")
          while True: 
               if secound.lower().strip() != "y" and secound.lower().strip() != "n":
                    print("Sorry, I didn't quit catch that...Please try again\n")
                    secound = input("Ask another question? Y/N\n")
                    continue 
               else : 
                    break

          if secound.lower().strip() == "y":
               print('"Sir, did you get angry?"')
               print('"Of course I got angry. Anyone would! I still am. That was my wife! I dont remember much about that morning. I stormed off after I found them."')
               print("Adding Count Chrispin to list of suspects...")
               suspects.append("Count Chrispin")
               recall_suspects()
          elif secound.lower().strip() == "n":
               print('"I better get going."')
               print("hmmm, if that were me I would get pretty angry. Maybe it was a crime of passion?... Adding Count Chrispin to list of suspects...")
               suspects.append("Count Chrispin")
               recall_suspects()

# User can recall suspects and guess whose guilty
def recall_suspects():
     print('Okay.. who are my suspects...', suspects)
     # User will type who is guilty here      
     guilty = input('Who do you think is guilty?...\n')
     while True:
          if guilty.lower().strip() != "count chrispin" and guilty.lower().strip() != "Clara" and guilty.lower().strip() != "major":
               print("Did you spell their names correctly? Please try again.\n")
               guilty = input('Who do you think is guilty?...\n')
               continue 
          else : 
               break

# suspect reveal 
def finale():
     print('"so, you think the murderer was"', guilty)
     if guilty == "major":
          print('"Okay! I confess! It was me! She was going to expose us, so I put posin in her breakfast. I would have lost everything!"')
     if guilty == "count chrispin":
          print("But Count Chrispin was not the last to see Lady Amara, he stormed off. It can't have been him.")
     if guilty == "clara":
          print("Clara was seen by a lot of people at the funfair. She's such a public figure, she was not seen any where near her mums tent.")
     print('The Major was charged for the murder of Lady Amara. Traces of posin were found in the autopsy. A letter addressed to the major was found on the corpse.')
     print('To my dearest Carter, I have to come clean to my husband. Our secret is killing me. I will love you always.')
     quit()

# main game functions
def main():
     game_start()
     walk()
     first_location()
     find_clara()
     find_the_major()
     find_count_crispin()
     recall_suspects()
     finale()

main()