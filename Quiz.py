
#allows us to access a random 'key' in the dictionary
import random

#the questions/answer dictionary
imibuzo =   {
                "How many rings on the Olympic flag" : "five",
                "During stand-ups, who always asks: What did you learn" : "cara",
                "Which animal is man's best friend" : "dog",
                "What is infront of women and at the back of cow" : "w",
                "Who had a long walk to freedom" : "mandela",
                "What did South Africa host in 2010" : "world cup",
                "What is the nickname of SA's national football team" : "bafana bafana",
                "What is the national flower of SA" : "protea",
                "Which city is known as the Mother City" : "cape town"
        
            }

#welcome message
print("CodeX Fun Quiz")
print("Put your answer in-between double qoutes when answering")
print("=======================")

#the quiz will end when this variable becomes 'False'
playing = True

#While the game is running
while playing == True:

    #set the score to 0
    score = 0

    #gets the number of questions the player wants to answer
    num = int(input("\nHow many questions would you like between 1 to 9: "))

    #loop the correct number of times
    for i in range(num):

        #the question is one of the dictionary keys, picked at random
        question = (random.choice( list(imibuzo.keys())))
        #the answer is the string mapped to the question key
        answer = imibuzo[question]

        #print the question, along with the question number
        print("\nQuestion " + str(i+1) )
        print(question  + "?")

        #get the user's answer attempt
        guess = input('')

        #if their guess is the same as the answer
        if guess.lower() == answer.lower():
            #add 1 to the score and print a message
            print("Correct!")
            score += 1
        else:
            print("Unfortunateley that's not the right answer!")

    #after the quiz, print their final score  
    print("\nYour final score was " + str(score))

    #store the user's input...
    again = input("Enter any key to play again, or 'q' to quit.")

    #... and quit if they types 'q'
    if again.lower() == 'q':
        playing = False