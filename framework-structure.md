# Framework Structure

This document serves to provide a clear structure of our Ontology-based Personalized Course Recommender System. 

Our framework consists **three parts**:
1. Career recommender
    - Matches the student's traits with job descriptions
2. HKU Program recommender
    - Admission requirements
    - Specific curriculum or course requirements
3. FAQ chatbot
    - Uses NLP model(s) to match student query with database

## 1. Career Recommender
The career recommender provides recommendations to the student's future career. 

**Data Collection**



## 2. HKU Program Recommender



## 3. FAQ Chatbot
The FAQ chatbot uses NLP model(s) to match the student's open-ended question/query with our database.

**Data Collection**
1. Internal FAQ database - scraped
2. Datasets for NLP model training
    - 
    - SQuAD 2.0 (The Stanford Question Answering Dataset) - not necessarily on educational material

**Model Training Trials**
1. q-Q similarity: Try basic word embedding models on internal FAQ database
    - CNN-rank (?)
2. q-A similarity: 
3. TSUBAKI