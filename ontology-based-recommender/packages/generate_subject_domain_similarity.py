import logging
from ast import List
import numpy as np
import pandas as pd

from ontology_profiles.student_profile.Student import *
from ontology_profiles.student_profile.PersonalInfo import *
from ontology_profiles.student_profile.EducationalInfo import *

from ontology_profiles.course_profile.Course import *
from ontology_profiles.course_profile.CourseBasicInfo import *
from ontology_profiles.course_profile.CourseContent import *

from ontology_profiles.course_profile.SubjectDomain import *


from helper_functions import *

from gensim.models import KeyedVectors, Word2Vec




def generate_individual_subject_domain_similarity(student: Student, subject_domain: SubjectDomain, model, similarity_type, threshold):
    subject_keywords = subject_domain.get_subject_domain_keywords()
    student_skills = student.get_skills()

    # similarity algorithm: calculate the average similarity between the student's skills and the keywords
    skills_similarities = []
    for skill in student_skills:
        word_similarities = []
        for keyword in subject_keywords:
            try:
                word_similarities.append(model.similarity(skill, keyword))
            except:
                word_similarities.append(0)
        filtered_word_similarities = [score for score in word_similarities if score > threshold]
        individual_skill_similarity = np.sum(filtered_word_similarities)
        skills_similarities.append(individual_skill_similarity)

    final_skills_similarity = np.mean(skills_similarities)

    return final_skills_similarity



def generate_all_subject_domain_similarities(student: Student, subject_domains: List, MODEL_PATH, similarity_type, threshold):
    all_subject_domain_similarities = []

    if similarity_type == 'cosine':
        # load model
        model = Word2Vec.load(MODEL_PATH).wv
        #model = KeyedVectors.load(MODEL_PATH)
    
    for subject in subject_domains:
        subject_domain_name = subject.get_subject_domain()
        keyword_matching_similarity_score = generate_individual_subject_domain_similarity(student, subject, model, similarity_type, threshold)
        all_subject_domain_similarities.append(
            [subject_domain_name, keyword_matching_similarity_score]
        )
    
    df = pd.DataFrame(
        all_subject_domain_similarities,
        columns=['Subject Domain', 'Similarity']
    ).sort_values(by='Similarity', ascending=False)

    return df
