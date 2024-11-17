import streamlit as st


st.write("This temporarily serves as the data management page; this should be hidden")

#DEFINITION OF CLASS USER
class User:

    def __init__(self, user_name, user_major, user_event_categories, user_keywords):
        self.user_name = user_name
        self.user_major = user_major
        self._user_event_categories = []
        self._user_keywords = []



#DEFINITION OF CLASS MAJOR
class Major:

    def __init__(self, major, major_keywords):
        self._major = major
        self._major_keywords = []



#DEFINITION OF CLASS SESSION STATE
class session_state_variables():

    def __init__(self, user_name, user_major, user_event_categories, user_keywords):
        self.user_name = user_name
        self.user_major = user_major
        self._user_event_categories = []
        self._user_keywords = []


#CLEARING SESSION STATES
def reset_session():
        if st.button("Reset all"):
            for key in st.session_state.keys():
                del st.session_state[key]


#SESSION STATE INSTANCES
session_state_1 = session_state_variables("name", "major", "event categories", "keywords")


#MAJOR INSTANCES - CREATE SEPARATE SECTION WITH LISTS AND ONLY INCLUDE LIST VARIABLES IN INSTANCES
test_major_BA = Major("Bachelor: BA", ["consulting", "business", "finance"])
test_major_Econ = Major("Bachelor: Econ", ["economics", "finance", "sustainability"])


#USER INSTANCES
test_user = User("", "", [""], [""])


#USER NAME
if session_state_1.user_name not in st.session_state:
    st.session_state[session_state_1.user_name] = ""

#USER MAJOR
if session_state_1.user_major not in st.session_state:
    st.session_state[session_state_1.user_major] = ""

#USER EVENT CATEGORIES
if session_state_1._user_event_categories not in st.session_state:
    st.session_state[session_state_1._user_event_categories] = []

#USER KEYWORDS
if session_state_1._user_keywords not in st.session_state:
    st.session_state[session_state_1._user_keywords] = []

st.write(st.session_state)






reset_session()