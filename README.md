# Hybrid Knowledge Chatbot

## Overview
This project is a Python-based chatbot that uses a JSON knowledge base to answer user queries. It applies fuzzy string matching to find the closest question and returns the stored answer.

If no match is found, the chatbot uses web scraping to fetch relevant information from the internet. New question-answer pairs are then stored automatically, allowing the system to improve over time.

## Features
- JSON-based knowledge storage for Q&A  
- Fuzzy matching using difflib for better input handling  
- Web scraping fallback using requests and BeautifulSoup  
- Self-learning system that updates knowledge base automatically  

## Technologies Used
- Python  
- JSON  
- difflib  
- requests  
- BeautifulSoup  

## Working Flow
1. User enters a question  
2. Chatbot checks local knowledge base  
3. If a match is found, it returns the answer  
4. If not, it scrapes web data for response  
5. New Q&A is saved into JSON for future use  

## Setup Instructions

Install required libraries:
pip install requests beautifulsoup4


Run the program:
python main.py


## Future Improvements
- Add GUI using Tkinter or Streamlit  
- Improve natural language processing accuracy  
- Replace JSON storage with a database system
