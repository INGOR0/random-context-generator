#These three are so I can work with time values, random values and json files
import random
import json



#This will load the databases I have

with open('nouns_database.json', 'r') as file:                         #Tells the program to not only open the file described to be opened and read, but also be closed after and be named "file" for shorten
    nouns_database = json.load(file)                                    #This is for creating a variable that refers to loading a json file in specific, in this case our database named "file"

with open('adjectives_database.json', 'r') as file2:                    #same thing as before, but with file2 because file is already in use
    adjectives_database = json.load(file2)

with open('actions_database.json', 'r') as file3:
    actions_database = json.load(file3)



#This is to generate the setting and action

def generate_random_setting():

    noun = random.choice(nouns_database["noun"])                        #Get a random noun from the database
    adjective = random.choice(adjectives_database["adjective"])         #Get a random adjective from the database

    setting = f"{adjective} {noun}"                                #Making a variable named setting that will be an adjective and a noun randomly selected. I use f string function to be able to put text in it

    return noun, adjective, setting                                                      #This gives back the 3 different variables


def generate_random_action():

    action = random.choice(actions_database["action"])

    return action


def generate_random_context():

    noun, adjective, setting = generate_random_setting()
    action = generate_random_action()

    context = f"In a {setting}, where char1 and char2 are {action}."

    return noun, adjective, setting, action, context



#variables outside the function to call these (I let that there to mention I was confused, I only need this one variable)

noun, adjective, setting, action, random_context = generate_random_context()

print("Random noun selected:", noun)
print("Random adjective selected:", adjective)
print("Random setting created:", setting)
print("Random action selected:", action)
print("Random context created:", random_context)