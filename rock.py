import random 

def startGame():
  player= input("Draw an option 'Rock', 'Paper', 'Scissors'\n")

  computer = random.choice(['Rock', 'Paper', 'Scissors'])

  if player == computer:
      return "both selected {}. Tie".format(computer)

  if is_win(player, computer):
      return "player selected {} and computer selected {} you won".format(player, computer) 

  return "player selected {} and computer selected {}. you Lost".format(player, computer)

def is_win(player1, opponent) :        
   if(player1 == 'Rock' and opponent == 'Scissors')  or (player1 == 'Scissors' and opponent == 'Paper') or (player1 == 'Paper' and opponent == 'Rock'):
      return True
   return False    

if __name__ == '__main__':
    print(startGame()) 