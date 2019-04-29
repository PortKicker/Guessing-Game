import random

the_num = random.randint(1,101) 

print('Hello! \n \n This is a number guessing game developed by NuGui. This game is fairly simple. I will pick a number between 1 and 100, then you will have to guess it. \n \n The rules are pretty simple. \n 1. If you guess a number less than 1 or greater than 100 you will be OUT OF BOUNDS! \n 2. Upon your first turn, I will tell you WARM if you are close, but COLD if you are not. \n 3. All turns after that I will tell you if you are getting WARMER of COLDER. \n Upon guessing the correct number, I will Give you a WIN along with the total amount of guesses it took you to WIN.\n \n Alright I have my number.\n \n ' ) 

lst_guess = [0] 

while True:
    player = int(input(" what's your guess? : " ))
    
    if player < 1 or player > 100:
        print('OUT OF BOUNDS')
        continue
    
    if player == the_num:
        print(f'you WIN! It only took you {len(lst_guess)} guesses!')
        break
    
    lst_guess.append(player)
    
    if lst_guess[-2]:
       if abs(the_num-player) < abs(the_num-lst_guess[-2]):
           print('WARMER')
       else:
           print('COLDER')


    else:
        if abs(the_num-player) <= 10:
               print('WARM') 
        else:
               print('COLD')
    
