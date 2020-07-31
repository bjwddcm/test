temp = input('input a number:')
guess = int(temp)

while guess != 8:
    if guess < 8:
        print('should be higher')
    else:
        print('should be lower')
        
    temp = input('try again:')
    guess = int(guess)
    
print('correct')