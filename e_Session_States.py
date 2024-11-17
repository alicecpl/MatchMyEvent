import streamlit as st

#IMPORT ALL INSTANCES OF CLASSES
from multipage_layout import test_user
from multipage_layout import test_major_BA
from multipage_layout import test_major_Econ


class session_state_variables():

    def __init__(self, user_name, user_major, user_event_categories, user_keywords):
        self.user_name = user_name
        self.user_major = user_major
        self._user_event_categories = []
        self._user_keywords = []

session_state_1 = session_state_variables("name", "major", "event categories", "keywords")





if test_user.user_name not in st.session_state:
    st.session_state[session_state_1.user_name] = 0

st.write(st.session_state)


#CLEARING SESSION STATES (reset-button to be implemented)

def reset_session():
    st.button("Reset all")
    if st.button:
        for key in st.session_state.keys():
            del st.session_state[key]

reset_session()