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