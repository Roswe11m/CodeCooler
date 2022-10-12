import random
print("Hellol! welcome to PycatAI!")
Version = input("Do you have a dev code? ")
if Version == "yes":
  devcode = input("what is the dev code? ")
  while True:
    if devcode == ("1357"):
     ask = input("What would you like to do? ")
      
    if ask == "search":
                  try:
                      from googlesearch import search
                  except ImportError:
                      print("No module named 'google' found")
                  
                  # to search
                  query = input("What would you like to search? ")
                  
                  for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                      print(j)
    elif ask == "games":
                  print("Find our games on the pycat games tab!")
    elif ask == "hi":
                  print("hello there!")
    elif ask == "hello":
                  print("Hello!")
    elif ask == "mines":
                  import random
                  #difficulty = input("What difficulty would you like? Easy medium or hard. Answer with E, M, or H").strip().lower()
                  yrn = ["y","n"]
                  #yrn2 = ["y", "n"]
                  #yrn3 = ["y", "n", "n"]
      
                  #if difficulty == "e":
                      
                  #1-9 options
                  one = random.choice(yrn)
                  two = random.choice(yrn)
                  three = random.choice(yrn)
                  four = random.choice(yrn)
                  five = random.choice(yrn)
                  six = random.choice(yrn)
                  seven = random.choice(yrn)
                  eight = random.choice(yrn)
                  nine = random.choice(yrn)
                  def Mines():
                      one = random.choice(yrn)
                      two = random.choice(yrn)
                      three = random.choice(yrn)
                      four = random.choice(yrn)
                      five = random.choice(yrn)
                      six = random.choice(yrn)
                      seven = random.choice(yrn)
                      eight = random.choice(yrn)
                      nine = random.choice(yrn)
                  #Message
                  print ("welcome to MineSweeper! WIP")
                  #input
                  #player_answer = input("Assuming you know how to play, choose a number from 1 to 9!")
                  #if statements
                  for x in range(1,9):
                      print("|1|2|3|")
                      print("|4|5|6|")
                      print("|7|8|9|")
                      Mines()
                      player_answer = input("Assuming you know how to play, choose a number from 1 to 9!")
                      if player_answer == "1":
                          if one == "y":
                              print("Correct!")
                          else:
                              print("You lost :(")
                              break         
                      elif player_answer == "2":
                          if two == "y":
                              print("Correct!")
                          else:
                              print("You lost :(")
                              break
                      elif player_answer == "3":
                          if three == "y":
                              print("Correct!")
                          else:
                              print("You lost :(")
                              break
                      elif player_answer == "4":
                          if four == "y":
                              print("Correct!")
                          else:
                              print("You lost :(")
                              break
                      elif player_answer == "5":
                          if five == "y":
                              print("Correct!")
                          else:
                              print("You lost :(")
                              break
                      elif player_answer == "6":
                          if six == "y":
                              print("Correct!")
                          else:
                              print("You lost :(")
                              break
                      elif player_answer == "7":
                          if seven == "y":
                              print("Correct!")
                          else:
                              print("You lost :(")
                              break
                      elif player_answer == "8":
                          if eight == "y":
                              print("Correct!")
                          else:
                              print("You lost :(")
                              break
                      elif player_answer == "9":
                          if nine == "y":
                              print("Correct!")
                          else:
                              print("You lost :(")
                              break
                          continue
              
    elif ask == "mathgame":
                  #give player 100 health and no points
                  health = 100
                  points = 10
                  #ask math question
                  while True:
                      x = random.randint(1,12)#random number 1-12
                      y = random.randint(1,12)#random number 1-12
                      answer =int( input (f"what is {x} times {y}? "))
                      if answer == x*y:
                          print ("Correct!")
                          print ("You gained 10 health and 1 points!")
                          health += 10
                          points += 1
                          print (f"You now have {health} health and {points} points")
                      else:
                          print ("WRONG!")
                          health -=10
                          print ("You lost 10 health.")
                          print (f"You now have {health} health and {points} points")
      
      
                  #out of health = game end if you have 50 points you get to stay in
                      if health <= 0:
                          if points <= 0: 
                              print ("GAME OVER")
                              break
                          elif points >= 10:
                              health = 50
                              points -= 10
                              print (f"you have been revived and have lost ten points, you now have {points} points and 50 health")
      
    elif ask == "math":
                  type = input("What type? D M S A ")
                  if type == ("D"):
                      X = int(input("first number "))
                      Y = int(input("second number "))
                      answer = X / Y
                      print(answer)
                  elif type == ("M"):
                      X = int(input("first number "))
                      Y = int(input("second number "))
                      answer = X * Y
                      print(answer)
                  elif type == ("S"):
                      X = int(input("first number "))
                      Y = int(input("second number "))
                      answer = X - Y
                      print(answer)
                  elif type == ("A"):
                      X = int(input("first number "))
                      Y = int(input("second number "))
                      answer = X + Y
                      print(answer)
    elif ask == "help":
      print("Here are some commands: search, games, mines, mathgame, tictac, and math.")
    elif ask == "tictac":
      #prints board
      board = [" "]*9
      
      def printboard():
          print(f" {board[0]} | {board[1]} | {board[2]} ")
          print(f" {board[3]} | {board[4]} | {board[5]} ")
          print(f" {board[6]} | {board[7]} | {board[8]} ")
      
      #function
      def turn(player):
          print(f"It is {player} turn")
          slot = int(input("what slot would you like to choose (1-9)"))
          if board[slot-1] == (" "):
              board[slot-1] = player
          else:
              print("That space is already taken, you lost a turn.")
      def is_victory(player):
          # If there's 3 in a row anywhere, return True, otherwise, return False
          if (board[0] == player and board[1] == player and board[2] == player) or \
             (board[3] == player and board[4] == player and board[5] == player) or \
             (board[6] == player and board[7] == player and board[8] == player) or \
             (board[0] == player and board[3] == player and board[6] == player) or \
             (board[1] == player and board[4] == player and board[7] == player) or \
             (board[2] == player and board[5] == player and board[8] == player) or \
             (board[0] == player and board[4] == player and board[8] == player) or \
             (board[2] == player and board[4] == player and board[6] == player):
              return True
          else:
              return False
          
      def playable():
          if " " not in board:
              return False
          else:
              return True
      
          
      while True:
          printboard()
          turn("X")
          if is_victory("X") == True:
              print("You win!")
              break
          if playable == False:
              print("It's a tie!")
              break
          printboard()
          turn("O")
          if is_victory("O") == True:
              print("You win!")
              break
          if playable == False:
              print("It's a tie!")
              break





















        
 
    else:
     print("That is not a valid command!")
     print("Here are some commands: search, games, mines, mathgame, tictac, and math. ")

  
else:
  print("Our free version has less features than the developer edition! Go to suggestions under the home tab to apply for dev mode! Thank you!")
  while True:
    askfree = input("What would you like to do? ")
    if askfree == "search":
                    try:
                        from googlesearch import search
                    except ImportError:
                        print("No module named 'google' found")
                    
                    # to search
                    query = input("What would you like to search? ")
                    print("This may take a second...")
                    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                  
                        print(j)
    
    elif askfree == "mines":
                    import random
                    #difficulty = input("What difficulty would you like? Easy medium or hard. Answer with E, M, or H").strip().lower()
                    yrn = ["y","n"]
                    #yrn2 = ["y", "n"]
                    #yrn3 = ["y", "n", "n"]
        
                    #if difficulty == "e":
                        
                    #1-9 options
                    one = random.choice(yrn)
                    two = random.choice(yrn)
                    three = random.choice(yrn)
                    four = random.choice(yrn)
                    five = random.choice(yrn)
                    six = random.choice(yrn)
                    seven = random.choice(yrn)
                    eight = random.choice(yrn)
                    nine = random.choice(yrn)
                    def Mines():
                        one = random.choice(yrn)
                        two = random.choice(yrn)
                        three = random.choice(yrn)
                        four = random.choice(yrn)
                        five = random.choice(yrn)
                        six = random.choice(yrn)
                        seven = random.choice(yrn)
                        eight = random.choice(yrn)
                        nine = random.choice(yrn)
                    #Message
                    print ("welcome to MineSweeper! WIP")
                    #input
                    #player_answer = input("Assuming you know how to play, choose a number from 1 to 9!")
                    #if statements
                    for x in range(1,9):
                        print("|1|2|3|")
                        print("|4|5|6|")
                        print("|7|8|9|")
                        Mines()
                        player_answer = input("Assuming you know how to play, choose a number from 1 to 9!")
                        if player_answer == "1":
                            if one == "y":
                                print("Correct!")
                            else:
                                print("You lost :(")
                                break         
                        elif player_answer == "2":
                            if two == "y":
                                print("Correct!")
                            else:
                                print("You lost :(")
                                break
                        elif player_answer == "3":
                            if three == "y":
                                print("Correct!")
                            else:
                                print("You lost :(")
                                break
                        elif player_answer == "4":
                            if four == "y":
                                print("Correct!")
                            else:
                                print("You lost :(")
                                break
                        elif player_answer == "5":
                            if five == "y":
                                print("Correct!")
                            else:
                                print("You lost :(")
                                break
                        elif player_answer == "6":
                            if six == "y":
                                print("Correct!")
                            else:
                                print("You lost :(")
                                break
                        elif player_answer == "7":
                            if seven == "y":
                                print("Correct!")
                            else:
                                print("You lost :(")
                                break
                        elif player_answer == "8":
                            if eight == "y":
                                print("Correct!")
                            else:
                                print("You lost :(")
                                break
                        elif player_answer == "9":
                            if nine == "y":
                                print("Correct!")
                            else:
                                print("You lost :(")
                                break
                            continue
    elif askfree == "help":
      print("Here are some commands: search, mines, tictac, and math.")                     
    elif askfree == "tictac":
      #prints board
      board = [" "]*9
      
      def printboard():
          print(f" {board[0]} | {board[1]} | {board[2]} ")
          print(f" {board[3]} | {board[4]} | {board[5]} ")
          print(f" {board[6]} | {board[7]} | {board[8]} ")
      
      #function
      def turn(player):
          print(f"It is {player} turn")
          slot = int(input("what slot would you like to choose (1-9)"))
          if board[slot-1] == (" "):
              board[slot-1] = player
          else:
              print("That space is already taken, you lost a turn.")
      def is_victory(player):
          # If there's 3 in a row anywhere, return True, otherwise, return False
          if (board[0] == player and board[1] == player and board[2] == player) or \
             (board[3] == player and board[4] == player and board[5] == player) or \
             (board[6] == player and board[7] == player and board[8] == player) or \
             (board[0] == player and board[3] == player and board[6] == player) or \
             (board[1] == player and board[4] == player and board[7] == player) or \
             (board[2] == player and board[5] == player and board[8] == player) or \
             (board[0] == player and board[4] == player and board[8] == player) or \
             (board[2] == player and board[4] == player and board[6] == player):
              return True
          else:
              return False
          
      def playable():
          if " " not in board:
              return False
          else:
              return True
      
          
      while True:
          printboard()
          turn("X")
          if is_victory("X") == True:
              print("You win!")
              break
          if playable == False:
              print("It's a tie!")
              break
          printboard()
          turn("O")
          if is_victory("O") == True:
              print("You win!")
              break
          if playable == False:
              print("It's a tie!")
              break





















        
 
    else:
      print("That is not a valid command.")
      print("Type 'help' for a list of commands") 
