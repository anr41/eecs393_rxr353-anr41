#Ashley Roberson
#This is the ReadMe file for the Alexa and plagiarism checker portion of Comprehensive Student Aide

Plagiarism Checker:
    The goal of the plagiarism checker was to allow students to see how correct their answers are to uploaded solutions on our website by seeing how similar the two files were. Although, I never got this portion working correctly, I tried integrating the copyLeaks API.  When running, it processes the two files and deducts credits from my account for invoking the API.  However there is one error at the end that I was not able to fix.
    
    Usage Instructions:
        Before running the copyleaks.py file, replace the text file name on line 19 in the declaration of files with a file on your desktop.  Then run the python file.  While the program is running, you should notice Processing... being displayed on your screen repeatedly until the program has finished.  I was never able to get the program to get past that point because of the error.
        
Alexa Flashcards Skill:
    Another feature of the Comprehensive Student Aide was to have students be able to study for their classes using Alexa.  To implement this, I attempted developing a flashcards skill for Alexa.  All of the skill for Alexa was developed using Amazon Web Services. I was unable to integrate this skill with Comprehensive Aide and don't know how to allow public access for testing the skill so I uploaded the code for the skill along with the testing code and results used from Amazon Web Services.
    The lambda function contains the code that makes the skill a flashcard skill.  The intent schema contains all of the possible valid intents that can be called when the user interacts with Alexa.  The sample utterances file contains all of the phrases that a user is able to say to Alexa.
    
    Usage Instructions:
        I am not sure how to make the code accessible to the public.  But, once the skill is published and certified, a user would begin studying the flashcards by first launching the program by saying, "open quizie."  Once the skill opens, Alexa gives a welcome response, "Welcome to Quizie. Let's begin:" followed by the first question in the stack of flashcards.  Then the user is supposed to respond with the correct answer.  Alexa then says if that was right or wrong and then delivers the next question.  Throughout the studying process, the user is able to ask Alexa for help if they don't know how to use this skill, cancel or quit if they want to stop, start over to restart the deck of flashcards, or for Alexa to repeat herself.
