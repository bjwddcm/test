print('----------------------------------------')



temp = input('input a number:')
guess = int(temp)

while guess and 8 == True:
    print('correct')
    
if guess < 8:
    print("higher")
else:
    print('lower')