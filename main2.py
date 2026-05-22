'''We Import this library because it provides the functionality to encode python objects to JSON formated files and decode as well'''
import json

'''This library provides the required tools for comparing sequence and generating information about their differences (difflib.get_close_matches()
in python find words that closely match a given word from a list)'''
from difflib import get_close_matches

import requests
from bs4 import BeautifulSoup
# Load the knowledge base from JSON file
def load_knowledge_base(file_path):
    # Opening the json file in reading mode
    with open(file_path,"r",encoding="utf-8") as file:
        # json.load() -> reads the Json file it converts JSON data to a python object
        data = json.load(file)
    # Return the acquired data
    return data

# Save the knowledge base from JSON file
def save_knowledge_base(file_path,data):
    # Opening the json file in writing mode
    with open(file_path,"w",encoding="utf-8") as file:
        '''json.dump() is used to save data into JSON file
        data is the object that we want to store
        file is the JSON file in which we are interested in writing
        indent = 2 means it adds 2 spaces so the JSON looks neat and readable'''
        json.dump(data,file,indent=2,ensure_ascii=False)

# Finds the closest matching question to what the user typed
def find_best_matches(user_question,question):
    '''user_question = Question asked by the user
    question = List of stored questions "in JSON file"
    n = 1 is no of best matches needed (here it's one)
    cutoff = 0.6 is the minimum similarity needed (Ranges from 0 to 1)'''
    matches = get_close_matches(user_question, question, n=1, cutoff = 0.6)
    # If matches are found
    if matches:
        # Return the first element
        return matches[0]
    # Otherwise
    else:
        # Return None
        return None

# Gets answer for the question
def get_answers_for_questions(question,knowledge_base):
    # Iterates throughout it's knowledge and finds the best match of the Question
    for i in knowledge_base["questions"]:
        # if question matches with the user's question then
        if i["question"] == question:
            #returns its answer
            return i["answer"]

# This function Scraps data from the 'sdgs.un.org' website      
def scrape_sdg_info(question):
    url = "https://sdgs.un.org/goals"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("h2")
    text_data = ""
    for p in paragraphs[:5]:
        text_data += p.get_text() + '\n'
    print("from web")
    return text_data

# Main function for the Chatbot where we integrate all the fefined function       
def chat_bot():
    # Loading the info from the LOAD_KNOWLEDGE_BASE function that we defined earlier
    knowledge_base = load_knowledge_base('knowledge_base.json')
    # This runs until broken 
    while True:
        '''input() takes input from the user whereas
        .lower() converts all the input to lowercase'''
        user_input = input('You: ').lower()
        
        # If user enters "quit" then the loop gets broken
        if user_input.lower() =='quit':
            # Stops the loop and ends the chatbot program
            break
        
        # Program stors all the questions in this empty list
        question_list = []
        # Loops through all the Q and A present in the Knowledge_base
        for i in knowledge_base["questions"]:
            # Creates a list of questions since get_close_matches() can't work with dictionaries 
            question_list.append(i["question"])
        # tries to find the closest question in the knowledge_base to what the user typed
        best_match = find_best_matches(user_input, question_list)
# best_match = find_best_matches(user_input, [i["question"] for i in knowledge_base["questions"]])
        if best_match:
            answer = get_answers_for_questions(best_match,knowledge_base)
            print(f"Bot: {answer}")
            print()

        else:
            print("Bot: Searching the web...")
            answer = scrape_sdg_info(user_input)
            print(f"Bot: {answer}")
            print()
            knowledge_base["questions"].append({"question": user_input,"answer": answer})
            save_knowledge_base("knowledge_base.json", knowledge_base)


chat_bot()
