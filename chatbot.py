# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 09:39:01 2020

@author: vishal
"""
#Import libraries
import random
from textblob import TextBlob

#Name and Nickname convo
print("Hello there, what is your name ?")
name = input()
print()
print("Do you have a nickname ? (Y/N)")
ans = input()
print()
if 'y' in ans.lower():
    print('What is it ?')
    nickname = input()
    print("That's a cool nickname, let's call you "+ nickname +" from now onwards !")
else:
    print("Thats ok "+name+ " is fine")
print()
#Greeting selection
greetings = ["How are you today "+ nickname +" ?",
             "Voila "+ nickname +" how you doing ?",
             "Namaste "+ nickname +", How's your day going ?",
             "What's up "+ nickname +" ?"]
print(random.choice(greetings))
ans = input()
blob = TextBlob(ans)
print()
'''(-1.0 to 1.0) where -1.0 states negative 0 neutral +1.0 positive 
polarity can use subjectivity also [0.0 to 1.0] 0.0 is objective and 1.0 
is subjective, Subjectives are personal feelings whereas objective are factual'''  

if blob.polarity > 0:
    print("That's good, glad to hear that")
else:
    print("No no, it's fine.")
print()
    
 #Random questions   
#Questions = ["Do you like Pune ? ", "What is your favourite cuisine ? ", 
#             "What are your thoughts about Netflix ? ", "What about Avengers Endgame ? ",
#             "Any of the classic 90's sitcoms ? "]
 
topics = ['Cricket', 'Netflix', 'Cuisine', 'Endgame', 'Trekking']

questions = ["Do you like ", "What about ", 
             "What are your thoughts about ", "What about ",
             "I would like your opinion on ",
             "Wanna talk about ",
             "Do you like "]

for i in range(0, random.randint(3, 4)):
    Question = random.choice(questions)
    questions.remove(Question)
    Topic = random.choice(topics)
    topics.remove(Topic)
    print(Question + Topic + ' ?')
    ans = input()
    blob = TextBlob(ans)
    print()
    if blob.polarity > 0.5:
        print("That's impressive, you must really like", Topic)
    elif blob.polarity > 0.1:
        print("It's nice to hear from you about", Topic)
    elif blob.polarity < -0.5:
        print("It looks like you dont like "+ Topic + " that much.")
    else:
        print('Thats a neutral way to describe', Topic)
    
#    if blob.subjectivity > 0.6:
#        print("and you are so biased")
#    elif blob.subjectivity > 0.3:
#        print("and you are quite concerned")
#    else:
#        print('and you are quite in to it')
print()

#Random Goodbyes
Goodbyes = ["It was nice talking to you, Bye "+nickname+ "we'll meet again soon.",
            "That's quite a chat for today, see ya "+ nickname+ " Have a great day ahead",
            "Well enough for today "+ nickname + ", will talk again soon. Ba bye",
            "You were a delight to talk to "+ nickname]
print(random.choice(Goodbyes))

