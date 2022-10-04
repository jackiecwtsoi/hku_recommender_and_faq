
---
## **IMPORTANT: DO NOT COMMIT CODE TO THE 'MAIN'/'MASTER' BRANCH !!!**
---

# Introduction

This is one of the three major parts of the DASC7600 Data Science Project course of the HKU MDASC programme. We develop a personalized HKU information recommender and Q&A system based on the established OPCR framework, which is a core part of the HKU metaverse chatbot's functionality.

There are two parts to this system:
1. [University and career related information recommender](recommender/)
2. [HKU FAQ/Q&A system](faq/)

# Setup
1. Follow both documents below to download the necessary models:
    - [Setup for the recommender](recommender/README.md)
    - [Setup for the FAQ/Q&A system](faq/README.md)
2. Install all necessary dependencies using your terminal:
    ```python
    pip install -r requirements.txt
    ```
# Running the Program
Currently the two parts need to be run separately.
- To run the **recommender** component, run the following in your terminal (the terminal directory should be this current folder):
    ```python
    python recommender/packages/trigger_recommender_workflow.py
    ```
- To run the **FAQ/Q&A** component, run the following in your terminal (the terminal directory should be this current folder):
    ```python
    python faq/trigger_faq_workflow.py
    ```

# Things to Note
## Database for Students Information
Our recommender system should store information of all student users who have interacted with our system. The database containing all students information is [here](recommender/data/students_database.csv).

**HOWEVER**, currently we have not implemented the function of adding a new student through the command line, so in order for the recommender program code to work, we need to enter an email that **is already stored in the database**. Currently we only have two student entries (tsoic1@connect.hku.hk and 1234@connect.hku.hk). Feel free to use these two emails to test the program code. 

If you wish to add more student entries using other emails, simply open the database CSV file in Excel and add the new entries.

---
## **THE ENTIRE PROGRAM IS A PROTOTYPE ONLY AS OF CURRENTLY.**
---
