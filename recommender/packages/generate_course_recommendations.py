'''
This is the layer where we generate course-related recommendations, 
which would later be weighted and aggregated to generate final recommendations for a particualr student.

The course-related recommendation types include:
- course_basic_info TODO
- course_content: course description and learning outcomes
- course_assessment TODO
'''

import pandas as pd

from hku_recommender_and_faq.recommender.packages.ontology_profiles.student_profile.Student import *
from hku_recommender_and_faq.recommender.packages.ontology_profiles.student_profile.PersonalInfo import *
from hku_recommender_and_faq.recommender.packages.ontology_profiles.student_profile.EducationalInfo import *

from hku_recommender_and_faq.recommender.packages.ontology_profiles.course_profile.Course import *
from hku_recommender_and_faq.recommender.packages.ontology_profiles.course_profile.CourseBasicInfo import *
from hku_recommender_and_faq.recommender.packages.ontology_profiles.course_profile.CourseContent import *

from hku_recommender_and_faq.recommender.packages.helper_functions import *
from hku_recommender_and_faq.recommender.packages.generate_course_similarity import *
from hku_recommender_and_faq.recommender.packages.configs import *
from hku_recommender_and_faq.recommender.packages.apis import course_database_api
from hku_recommender_and_faq.recommender.packages.UserBasedCFCourseRecommender import UserBasedCFCourseRecommender

'''
FUNCTION
- Generate top k COURSE recommendations for the particular student
Return: DATAFRAME consisting of top k recommendations (Course Code)
'''
def generate_course_recommendations(student: Student, COURSE_REC_TYPES: list, COURSE_BASE_DATA_PATH, COURSE_ADDITIONAL_DATA_PATH_DICT, similarity_type='cosine', k=5):
    # 1. convert course dataset into a list of Course instances
    courses = course_database_api.convert_to_courses(COURSE_BASE_DATA_PATH, COURSE_ADDITIONAL_DATA_PATH_DICT)

    # 2. generate all similarity scores by comparing the student provided info and all courses in our database
    # TODO: need to change this to incorporate the LIST of course rec types instead of only one type
    df_course_content_similarities, actual_string = generate_all_course_similarities(student, courses, COURSE_MODEL_PATHS_DICT[COURSE_REC_TYPES[0]], similarity_type, COURSE_REC_TYPES[0])

    # 3. generate scores using the additional user-based collaborative filtering recommender
    user_based_cf_recommender = UserBasedCFCourseRecommender(actual_string)
    df_user_based_cf_scores = user_based_cf_recommender.get_df_cf_scores()

    # 4. Add a new column which is course code + course title
    df_course_content_similarities['Final'] = df_course_content_similarities['Course Code'] + ': ' + df_course_content_similarities['Course Title']

    # 5. left join 'df_course_content_similarities' and 'df_user_based_cf_scores', and get the final combined score
    df_recommendations = pd.merge(
        df_course_content_similarities, df_user_based_cf_scores,
        left_on='Final', right_on='Course', how='left'
    )
    df_recommendations['CF Score'] = df_recommendations['CF Score'].fillna(0) # replace NaN values with 0 in the 'CF Score' column
    df_recommendations['Final Score'] = 0.7*df_recommendations['Course cosine Similarity'] + 0.3*df_recommendations['CF Score']

    # 6. get the top k recommendations
    df_recommendations = df_recommendations.sort_values(by='Final Score', ascending=False).head(k)

    logging.info(f'Our top {k} course recommendations and their respective scores are:\n{df_recommendations}')

    return df_recommendations['Final'].values.tolist(), actual_string