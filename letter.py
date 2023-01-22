print("guess the word")
secret_word="PYTHONproject12345"
letter_guess=""
failure_count=3
while failure_count>0:
    guess=input("enter a letter :_")
    if guess in secret_word:
        print(f"correct! There is one or more {guess} in the secret word ")
    else:
        failure_count-=1
        print(f"incorrect! There is no {guess} in the secret word {failure_count} attemps remaining")
        
    letter_guess=letter_guess+guess
    wrongletter_count=0
    for letter in secret_word:
       if letter in letter_guess:
           print(f"{letter}",end=" ")
       else: 
           print("_",end=" ")
           wrongletter_count+=1
    print(" ")          
    if wrongletter_count==0:
        print(f"congratulation! the secret word was {secret_word} you won")
        break
else:
    print("sorry! you didn't win this time! try again")