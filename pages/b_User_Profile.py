import streamlit as st

#IMPORT ALL INSTANCES OF CLASSES
from multipage_layout import test_user
from multipage_layout import test_major_BA
from multipage_layout import test_major_Econ
from multipage_layout import session_state_1


st.write("This is purely an input page; nothing will be displayed here except what the user has selected")

#def update_name(user_name_input):
    #st.session_state[session_state_1.user_name] = user_name_input

def get_user_profile():
    st.subheader("User Profile")
    st.write("Please answer the questions below to create your User Profile")

    #NAME
    st.session_state[session_state_1.user_name] = st.text_input("What is you name?")# on_change=update_name)
    
    


    #MAJOR
    st.session_state[session_state_1.user_major] = st.selectbox("What is your major?", ("Bachelor: BA","Bachelor: Econ", "Bachelor: IA",
                                                                "Bachelor: Law & Econ", "Master: MacFin", "Master: MBI"),) #to be completed
    #test_user.user_major = session_state_1.user_major

    if st.session_state[session_state_1.user_major] == "Bachelor: BA":
        test_user._user_keywords = test_user._user_keywords + test_major_BA._major_keywords #appended list should reference predefined list; expand to include all majors
    elif st.session_state[session_state_1.user_major] == "Bachelor: Econ":
        for keyword in test_major_Econ._major_keywords:
            session_state_1._user_keywords.append(keyword)


    #EVENT TYPES
    event_type_selection = st.multiselect("Select all event types you are interested in", ["networking", "social", "workshop", "career", "podium_discussion"],)
    test_user._user_event_categories += event_type_selection #test


    #TEST ONLY - to be removed
    st.subheader("TESTING")
    st.write("TEST entries:")
    st.write("User Name: ", st.session_state[session_state_1.user_name])
    st.write("User Major: ", st.session_state[session_state_1.user_major])
    st.write("Major keywords: ", test_major_Econ._major_keywords)
    st.write("Event Categories: ", test_user._user_event_categories)
    st.write("User Keywords: ", test_user._user_keywords)
    st.write(test_user)


get_user_profile()

#st.write(type(test_user._user_event_categories))
#st.write(type(test_user._user_keywords))
#st.write(type(test_major_Econ._major_keywords))