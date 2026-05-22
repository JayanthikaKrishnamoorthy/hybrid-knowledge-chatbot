# Hybrid Knowledge Chatbot 🤖

Self-Learning Python Chatbot with Web Scraping and Fuzzy Matching

---

## 📌 Overview

A Python-based chatbot that answers user queries using a local JSON knowledge base and improves itself over time.

The system uses:
- Fuzzy string matching (difflib)
- Web scraping (requests + BeautifulSoup)
- JSON-based knowledge storage
- Self-learning Q&A updates

This project demonstrates how simple AI concepts, web data extraction, and memory systems can be combined into a smart assistant.

---

# 🚀 Features

✅ JSON-based Knowledge Base  
✅ Fuzzy Matching for similar questions  
✅ Web Scraping fallback for unknown queries  
✅ Automatic learning and data storage  
✅ Continuous improvement with usage  

---

# 🛠️ Technologies Used

- Python  
- JSON  
- difflib  
- requests  
- BeautifulSoup  

---

# ⚙️ System Workflow

## 1. User Input
User enters a question in natural language.

## 2. Knowledge Base Search
System searches JSON file using fuzzy matching.

## 3. Response Handling
- If match found → return stored answer  
- If not found → trigger web scraping  

## 4. Web Scraping
Extracts relevant information from online sources.

## 5. Learning Phase
New Q&A is stored in JSON for future use.

---

# 📊 Core Components

## Fuzzy Matching
Used to identify closest matching questions even with spelling variations.

## Web Scraping Engine
Fetches live information from external websites when no local match exists.

## Knowledge Base
Stores all learned question-answer pairs in structured JSON format.

---

# 📈 System Behavior

| Case | Action |
|------|------|
| Known Question | Returns stored answer |
| Similar Question | Uses fuzzy matching |
| Unknown Question | Scrapes web data |
| New Query | Stores in knowledge base |

---

# 📁 Project Structure

```bash
Hybrid-Chatbot/
│
├── knowledge_base.json
├── chatbot.py
├── README.md
└── requirements.txt
