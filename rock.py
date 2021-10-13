import random 
import math

def startGame():
  player= input("Draw an option 'Rock', 'Paper', 'Scissors'\n")

  computer = random.choice(['Rock', 'Paper', 'Scissors'])

  if player == computer:
      return (0,player,computer)

  if is_win(player, computer):
      return (1,player,computer)

  return (-1,player,computer)

def is_win(player1, opponent) :        
   if(player1 == 'Rock' and opponent == 'Scissors')  or (player1 == 'Scissors' and opponent == 'Paper') or (player1 == 'Paper' and opponent == 'Rock'):
      return True
   return False    

def result_game(n):
    player1_win = 0
    opponent_win = 0
    win_necessary = math.ceil(n/2)
    while player1_win < win_necessary and opponent_win < win_necessary:
         result, player, computer = startGame()
         if result == 0:
             print('tie game as you both have chosen {}.\n'.format(player))
         elif  result == 1:  
              player1_win += 1
              print('player selected {} and computer selected {}. you won\n'.format(player, computer)) 
         else: 
               opponent_win += 1
               print('player selected {} and computer selected {}. you Lost\n'.format(player, computer)) 
         print('\n')
    if  player1_win> opponent_win:

        print ('you won')   
    else: 
        print ('Unfortunately you Lost')              
        


    print(win_necessary)
if __name__ == '__main__':

    result_game(5)
   # print(startGame()) 