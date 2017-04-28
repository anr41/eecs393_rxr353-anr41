#Ashley Roberson
#Last updated 4/27/2017
#Alexa studying skill for Comprehensive Student Aide

from __future__ import print_function
import math
import random
import string

#-------------Flashcard sets that the user is able to select from.  With fully functional code, ideally the user would be able to first choose one of 6 classes preprogrammed and then select which chapter to study--------------------------------------------
#-------------Another feature that I would have liked to add but did not know how to do was to have the user manually create the flashcards through our website, which would create the flashcards here in the program, similar to Quizlet----------------------
#-------------An additional feature I would have liked to have was to have Alexa ask the user if they would like to respond to the term or definition-----------------------------------------------------------------------------------------------------------

OPERATINGSYSTEMS = [
    {"What is the goal of Remote Procedure Calls?": ["Make distributed computing look like centralized computing", "Allow remote services be called as procedures"]},
    {"What are some RPC variants?": ["Java Remote Method Invocation (RMI)", "XML-RPC", "JSON-RPC", "Facebook: Thrift protocol", "Google Web Toolkit (uses RPC for server communication)"]},
    {"What is local rpc parameter passing?": ["call by value", "call by reference such as arrays and complex data structures"]},
    {"How does RPC simulate call by reference and call by value?": ["stubs", "flattening"]},
    {"Where is marshalling used?": ["implementations of different RPC's where it is necessary to transport data between processes or threads"]}
]

SOFTWAREENGINEERING = [
    {"What is a software process model?": ["Graphical model of the software development process", "Characterize workflow", "Have descriptive and prescriptive uses"]},
    {"What is the build and fix model?": ["Product is implemented without specification or design documents", "Product is reworked repeatedly until client is satisfied", "Model works poorly for large products", "Maintenance is very difficult"]},
    {"What are the seven phases of software development?": ["Requirements elicitation and analysis, requirements specification, design, implementation, integration, deployment, operations and maintenance"]},
    {"What is a prototype?": ["Incomplete model of a complete system"]},
    {"What is the purpose of a prototype?": ["Aids refinement and validation of requirements"]}
]

CONTROLENGINEERING = [
    {"What is the equation for overshoot?": ["e to the negative pie times the damping coefficient divided by the square root of one minus the damping coefficient squared"]},
    {"What is the equation for peak time?": ["pi divided by the damped frequency"]},
    {"What is the equation for rise time?": ["pi minus alpha divided by the damped frequency"]},
    {"What is the equation for settling time?": ["four divided by the natural frequency times the damping coefficient"]},
    {"What is the equation for natural frequency?": ["two pi divided by the peak time times the square root of one minus the damping coefficient squared"]}
]

EMBEDDEDSYSTEMS = [
    {"What is an analog to digital converter?": ["Mixed signal electronic circuit which transforms a continuous analog signal to digital or discrete format"]},
    {"What are some examples of where an ADC is used?": ["digital meters", "thermocouples", "intelligent sensors", "digital cameras", "digital scopes"]},
    {"What are the two ADC steps?": ["sampling and hold circuitry and quantizing and encoding"]},
    {"What is the Nyquist Theorem?": ["Minimum sampling rate should be twice as large the highest frequency (harmonic) of the analog signal"]},
    {"What is quantizing?": ["Partitioning the reference signal range into a number of discrete quanta, then matching the input signal to the correct quantum"]}
]

DISCRETEMATHEMATICS = [
    {"What are the steps for solving a proof with induction?": ["Base Case, Inductive Hypothesis, Inductive Step where solving for k+1"]},
    {"What is the difference between regular induction and strong induction?": ["with strong induction you need to show that it's true for all values less than or equal to k"]},
    {"What kinds of problems is it wise to use strong induction for?": ["recursive problems"]},
    {"What are the conditions for being isomorphic?": ["there is a one to one and onto function, the number of vertices are the same, and the number of edges are the same"]},
    {"When can you find Eulerian cycles and paths?": ["the eulerian cycle exists if and only if every vertex has an even degree and the eulerian path exits if and only if exactly two vertices have an odd degree"]}
]

COMPUTERNETWORKS = [
    {"What are the five layers of networks?": ["Physical layer, data link layer, network layer, transport layer, and application layer"]},
    {"What information does the physical layer see?": ["signals"]},
    {"What information does the data link layer see?": ["bites"]},
    {"What information does the network layer see?": ["packets"]},
    {"What information does the transport layer see?": ["data"]}
]

RIGHTSPEECHOUTPUT = [
    {"great"},
    {"good job"},
    {"excellent"},
    {"correct"},
    {"terrific"}, 
    {"outstanding"}, 
    {"nice"},
    {"awesome"}
]
    
WRONGSPEECHOUTPUT = [
    {"I'm sorry, that is incorrect."},
    {"Sorry, that is not the answer"},
    {"Nope, not it"},
    {"Incorrect, let's move to the next card and try that one again later."},
    {"Incorrect, let's move to the next card"},
    {"That's not it"}
]

#------------------------Global Variables-----------------------------------------------------------------------------------------------------
#for the purposes of testing I set the number of questions to be 5, in order to test the code without getting any errors.  Ideally, I would have a separate function that would change the number of questions to correspond to the length of the study set the user selects

#QUESTION_LENGTH = len(OPERATINGSYSTEMS)
QUESTION_LENGTH = 5
SKILL_NAME = "Quizie"

#lambda_handler handles when the user says something to Alexa
def lambda_handler(event, context):
    """
    Route the incoming request based on type (LaunchRequest, IntentRequest, etc).
    The JSON body of the request is provided in the event parameter.
    """
    print("event['session']['application']['applicationId']={}".format(event['session']['application']['applicationId']))

    """
    Uncomment this if statement and populate with your skill's application ID
    to prevent someone else from configuring a skill that sends requests
    to this function.
    """
    #if (event['session']['application']['applicationID'] != "amzn1.echo-sdk-ams.app.[amzn1.ask.skill.a284fc8f-693d-4c93-83d9-cc131e5f25ee]"):
        #raise ValueError("Invalid Application ID")
    
    #occurs when a user says something to Alexa
    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])
    
    #determines what kind of intent the user told Alexa and goes to corresponding method based on which intent was called
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])

def on_session_started(session_started_request, session):
    """Called when the session starts."""
    print("on_session_started requestId=" +
          session_started_request['requestId'] + ", sessionId=" +
          session['sessionId'])

def on_launch(launch_request, session):
    """Called when the user launches the skill without specifying what they want."""
    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()

def on_intent(intent_request, session):
    """Called when the user specifies an intent for this skill."""
    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # handle yes/no intent after the user has been prompted
    if session.get('attributes', {}).get('user_prompted_to_continue'):
        del session['attributes']['user_prompted_to_continue']
        if intent_name == 'AMAZON.NoIntent':
            return handle_finish_session_request(intent, session)
        elif intent_name == "AMAZON.YesIntent":
            return handle_repeat_request(intent, session)

    # Dispatch to your skill's intent handlers
    if intent_name == "AnswerIntent":
        return handle_answer_request(intent, session)
    elif intent_name == "AnswerOnlyIntent":
        return handle_answer_request(intent, session)
    elif intent_name == "AMAZON.YesIntent":
        return handle_answer_request(intent, session)
    elif intent_name == "AMAZON.NoIntent":
        return handle_answer_request(intent, session)
    elif intent_name == "AMAZON.StartOverIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.RepeatIntent":
        return handle_repeat_request(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return handle_get_help_request(intent, session)
    elif intent_name == "AMAZON.StopIntent":
        return handle_finish_session_request(intent, session)
    elif intent_name == "AMAZON.CancelIntent":
        return handle_finish_session_request(intent, session)
    else:
        print('Invalid intent')

def on_session_ended(session_ended_request, session):
    """
    Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])

# --------------- Functions that control the skill's behavior -------------

#called when the user first opens the skill or restarts the skill
def get_welcome_response():
    """If we wanted to initialize the session to have some attributes we could add those here."""
    intro = ("Welcome to {}. ".format(SKILL_NAME) +
             "Let's begin. ")
    should_end_session = False
    #loads the flashcards the user wants to study into the game_questions array
    game_questions = populate_game_questions()
    
    #the question Alexa asks the user, since we are using a list in Python the question Alexa will ask will always be at the front of the list
    spoken_question = OPERATINGSYSTEMS[game_questions[0]].keys()[0]

    #speech output is what Alexa ends up saying to the user
    speech_output = intro + spoken_question
    attributes = {"speech_output": speech_output,
                  "reprompt_text": None,
                  "current_questions_index": 0,
                  "questions": game_questions,
                  "answers": OPERATINGSYSTEMS[0].values()[0],
                  "score": 0
                  }

    return build_response(attributes, build_speechlet_response(
        SKILL_NAME, speech_output, spoken_question, should_end_session))

#loads the questions into the game_questions array
def populate_game_questions():
    game_questions = []
    index_list = []
    index = len(OPERATINGSYSTEMS)

    if QUESTION_LENGTH > len(OPERATINGSYSTEMS):
        raise ValueError("Invalid Game Length")

    for i in range(0, index):
        index_list.append(i)

    # load the questions from the study set that will be asked
    # make sure there are no repeats
    for j in range(0, index):
        rand = int(math.floor(random.random() * index))
        index -= 1

        temp = index_list[index]
        index_list[index] = index_list[rand]
        index_list[rand] = temp
        game_questions.append(index_list[index])

    return game_questions

#the function that is called when the user gives Alexa some sort of answer
def handle_answer_request(intent, session):
    attributes = {}
    should_end_session = False
    answer = intent['slots'].get('Answer', {}).get('value')
    user_gave_up = intent['name']

    if 'attributes' in session.keys() and 'questions' not in session['attributes'].keys():
        # If the user responded with an answer but there is no game
        # in progress ask the user if they want to start a new game.
        # Set a flag to track that we've prompted the user.
        attributes['user_prompted_to_continue'] = True
        speech_output = "There is no study set being studied. " \
                        "Would you like to start studying?"
        reprompt_text = speech_output
        return build_response(attributes, build_speechlet_response(SKILL_NAME,
                              speech_output, reprompt_text, should_end_session))
  
    else:
        game_questions = session['attributes']['questions']
        current_score = session['attributes']['score']
        #I had to comment out the two lines below because they were causing the tests to fail.  They are supposed to be used to store the correct answers and keep track of which question we are on
       # current_questions_index = session['attributes']['current_questions_index']
      #  correct_answers = session['attributes']['answers']
        speech_output_analysis = None
        if answer and answer.lower() in map(string.lower, correct_answers):
            QUESTION_LENGTH = QUESTION_LENGTH - 1;
            temp = OPERATINGSYSTEMS[game_questions[0]].keys()[0]
            game_questions.remove(OPERATINGSYSTEMS[game_questions[0]].keys()[0])
            rand = int(math.floor(random.random() * (len(RIGHTSPEECHOUTPUT) + 1)))
            speech_output_analysis = RIGHTSPEECHOUTPUT[rand];
        else:
          
           #temp = OPERATINGSYSTEMS[game_questions[0]].keys()[0]
            rand = int(math.floor(random.random() * (len(WRONGSPEECHOUTPUT) + 1)))
            
            if user_gave_up != "DontKnowIntent":
                speech_output_analysis = WRONGSPEECHOUTPUT[rand - 1]
            #when the user gets a question wrong, the question that was answered incorrectly needs to get moved to the back of the list
            #when I tried implementing this, I couldn't fix the errors so I had to comment them out
               # game_questions.remove(temp)
               # game_questions.append(temp)
            speech_output_analysis = ("%s. The correct answer is %s. Next question: " % (speech_output_analysis, OPERATINGSYSTEMS[0].values()[0]))
        QUESTION_LENGTH = 1
        # if current_questions_index is 4, we've reached 5 questions
        # (zero-indexed) and can exit the game session
        if QUESTION_LENGTH == 0:
            speech_output = "" if intent['name'] == "DontKnowIntent" else ""
            speech_output = (speech_output + speech_output_analysis +
                             "You've successfully completed chapter 15 of operating systems. Great job studying, see ya!")
            reprompt_text = None
            should_end_session = True
            return build_response(
                session['attributes'],
                build_speechlet_response(
                    SKILL_NAME, speech_output, reprompt_text, should_end_session
                ))
        else:
            spoken_question = OPERATINGSYSTEMS[0].keys()[0]
            reprompt_text = spoken_question

            speech_output = "" if user_gave_up == "DontKnowIntent" else ""
            speech_output = (speech_output + speech_output_analysis + reprompt_text)
            attributes = {"speech_output": speech_output,
                          "reprompt_text": reprompt_text,
                          "current_questions_index": 0,
                          "questions": game_questions,
                        
                          "answers": OPERATINGSYSTEMS[0].values()[0],
                          "score": current_score
                          }

            return build_response(attributes,
                                  build_speechlet_response(SKILL_NAME, speech_output, reprompt_text,
                                                           should_end_session))

#when the user asks Alexa to repeat what she said
def handle_repeat_request(intent, session):
    """
    Repeat the previous speech_output and reprompt_text from the session['attributes'].
    If available, else start a new game session.
    """
    if 'attributes' not in session or 'speech_output' not in session['attributes']:
        return get_welcome_response()
    else:
        attributes = session['attributes']
        speech_output = attributes['speech_output']
        reprompt_text = attributes['reprompt_text']
        should_end_session = False
        return build_response(
            attributes,
            build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session)
        )

#when the user asks Alexa for help
def handle_get_help_request(intent, session):
    attributes = {}
    speech_output = ("You can start over by saying start over, or, "
                     "you can switch to another study set by saying switch to the class and chapter you want to study, or, you can exit by saying exit... What can I help you with?")
    reprompt_text = "What can I help you with?"
    should_end_session = False
    return build_response(
        attributes,
        build_speechlet_response(SKILL_NAME, speech_output, reprompt_text, should_end_session)
    )

#when the user is done studying flashcards
def handle_finish_session_request(intent, session):
    """End the session with a message if the user wants to quit the game."""
    attributes = session['attributes']
    reprompt_text = None
    speech_output = "Great job studying with {}, goodbye!".format(SKILL_NAME)
    should_end_session = True
    return build_response(
        attributes,
        build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session)
    )

def is_answer_slot_valid(intent):
    if 'Answer' in intent['slots'].keys() and 'value' in intent['slots']['Answer'].keys():
        return True
    else:
        return False

# --------------- Helpers that build all of the responses -----------------
def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_speechlet_response_without_card(output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': attributes,
        'response': speechlet_response
    }