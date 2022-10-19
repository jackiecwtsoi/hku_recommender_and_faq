import logging
import numpy as np
import pandas as pd

from hku_recommender_and_faq.recommender.packages.ontology_profiles.student_profile.Student import *
from hku_recommender_and_faq.recommender.packages.ontology_profiles.student_profile.PersonalInfo import *
from hku_recommender_and_faq.recommender.packages.ontology_profiles.student_profile.EducationalInfo import *

from hku_recommender_and_faq.recommender.packages.ontology_profiles.course_profile.Course import *
from hku_recommender_and_faq.recommender.packages.ontology_profiles.course_profile.CourseBasicInfo import *
from hku_recommender_and_faq.recommender.packages.ontology_profiles.course_profile.CourseContent import *

from hku_recommender_and_faq.recommender.packages.ontology_profiles.course_profile.SubjectDomain import *


from hku_recommender_and_faq.recommender.packages.helper_functions import *

from gensim.models import KeyedVectors, Word2Vec




def generate_individual_subject_domain_similarity(student: Student, subject_domain: SubjectDomain, model, similarity_type, threshold):
    subject_keywords = subject_domain.get_subject_domain_keywords()
    student_skills = student.get_skills()
    job_aspiration = student.get_educational_info().get_job_aspiration()
    student_interest = student.get_educational_info().get_student_interest()

    # concatenate all three attributes (student_interest, job_aspiration, skills) to form a string which is then used to generate the similarity score
    student_info = student_interest + '; ' + job_aspiration + '; ' + student_skills
    logging.debug(f'The student information based on historical inputs is:\n{student_info}')

    # similarity algorithm: calculate the average similarity between the student's skills and the keywords
    similarities = []
    for info in student_info:
        word_similarities = []
        for keyword in subject_keywords:
            try:
                word_similarities.append(model.similarity(info, keyword))
            except:
                word_similarities.append(0)
        filtered_word_similarities = [score for score in word_similarities if score > threshold]
        individual_skill_similarity = np.sum(filtered_word_similarities)
        similarities.append(individual_skill_similarity)

    final_skills_similarity = np.mean(similarities)

    return final_skills_similarity



def generate_all_subject_domain_similarities(student: Student, subject_domains: list, MODEL_PATH, similarity_type, threshold):
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
