import json
import random
import time
import sys

###

with open('nouns_database.json', 'r') as nouns_file, \
     open('adjectives_database.json', 'r') as adjectives_file, \
     open('actions_database.json', 'r') as actions_file:

     nouns = json.load(nouns_file)
     adjectives = json.load(adjectives_file)
     actions = json.load(actions_file)
###

def generate_random_setting():

    if not nouns["nouns"] or not adjectives["adjectives"]:
        raise ValueError("Nouns or adjectives database is empty.")

    noun = random.choice(nouns["nouns"])
    adjective = random.choice(adjectives["adjectives"])
    setting = f"{adjective} {noun}"

    return noun, adjective, setting


def generate_random_action():

    if not actions["actions"]:
        raise ValueError("Actions database is empty.")

    action = random.choice(actions["actions"])

    return action


def generate_random_context():

    noun, adjective, setting = generate_random_setting()
    action = generate_random_action()

    context = f"In a {setting}, where Char1 and Char2 are {action}."

    return context

###

contexts_database = 'contexts_database.json'

def save_to_database(context):
    
    try:

        with open(contexts_database, 'r') as contexts_file:
            existing_data = json.load(contexts_file)

    except (FileNotFoundError, json.JSONDecodeError):

     existing_data = {"contexts": []}

    if context in existing_data["contexts"]:

        print(f"Context already exists: {context}")

    else:

        existing_data["contexts"].append(context)

        with open(contexts_database, 'w') as contexts_file:
            json.dump(existing_data, contexts_file, indent=4)

    print(f"Context: {context}")

###

def generate_by_time():

    while True:

        print("For how many seconds do you want the program to run?")
                    
        try:
                        
            seconds_chosen = int(input())
            start_time = time.time()
            contexts_counted = 0

            if seconds_chosen <= 0:

                print("Please, enter a valid number.")

                continue

            else:
                            
                while time.time() - start_time < seconds_chosen:

                    context = generate_random_context()
                    save_to_database(context)
                    contexts_counted += 1

                contexts_per_second = contexts_counted / seconds_chosen

                print(f"{contexts_counted} contexts have been generated in {seconds_chosen} seconds ({contexts_per_second}/s).")

                continue_generating()

                

        except ValueError:

            print("Please, enter a valid number.")

            continue


def generate_certain_number():
    
    while True:
        
        print("How many contexts would you like to generate?")

        try:

            number_chosen = int(input())
            start_time = time.time()
            contexts_counted = 0

            if number_chosen <= 0:

                print("Please, enter a valid number.")

                continue

            else:

                while contexts_counted < number_chosen:
                    
                    context = generate_random_context()
                    save_to_database(context)
                    contexts_counted += 1
                    elapsed_time = time.time() - start_time

                contexts_per_second = contexts_counted / elapsed_time

                print(f"{contexts_counted} contexts have been generated in {elapsed_time} seconds ({contexts_per_second}/s).")

                continue_generating()

        except ValueError:

            print("Please, enter a valid number.")


def continue_generating():

    print("Would you like to keep generating contexts? (y/n).")

    while True:

        yes_or_no = input().lower()

        if yes_or_no == "y":

            print("Would you like to change the generation mode? (y/n).")

            second_yes_or_no = input().lower()

            if second_yes_or_no == "y":

                use_the_program()

            elif second_yes_or_no == "n":

                print("Continuing in the current mode.")

                return
        
        elif yes_or_no == "n":

            print("Okay. The program will close automatically after 5 seconds.")

            time.sleep(5)

            sys.exit()
        
        else:

            print("Command not recognized. Try again.")

            continue

def use_the_program():

    print("Would you like to generate for x seconds or would you like to generate x amount of contexts? (seconds/number).")

    while True:

        seconds_or_number = input().lower()

        if seconds_or_number == "seconds":

            generate_by_time()

        elif seconds_or_number == "number":

            generate_certain_number()

        else:

            print("Command not recognized. Try again.")

            continue

###

def program_started():

    while True:

        user_input = input().lower()

        if user_input == "y":

            use_the_program()

        elif user_input == "n":

            print("Okay. The program will close automatically after 5 seconds.")

            time.sleep(5)

            sys.exit()

        else:

            print("Command not recognized. Try again.")

            continue

if __name__ == "__main__":
    
    print("Welcome to RaCoGen 2.0. Do you want to begin setting up the generation process? (y/n).")

    program_started()