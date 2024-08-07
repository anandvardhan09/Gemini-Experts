import streamlit as st
import Experts.ats as ats
import Experts.youtubeTranscripter as youtubeTranscripter
import Experts.nutritionExpert as nutritionExpert 

st.set_page_config(page_title="Gemini Experts")

st.markdown("<h1 style='text-align: center; padding: 50px; margin-top:0px;'>Gemini Experts</h1>", unsafe_allow_html=True)

col1, col2, col3, = st.columns([1,1,1])  # Adjust column ratios as needed

with col1:
    if st.button("ATS Expert"):
        st.session_state.page = "ats_page"
        
with col2:
    if st.button("Youtube Transcripter"):
        st.session_state.page = "youtube_transcripter_page"
with col3:
    if st.button("Nutrition Expert"):
        st.session_state.page = "nutritionExpert_page"



# Initialize session state for page
if "page" not in st.session_state:
    st.session_state.page = "ats_page"

# Page routing
if st.session_state.page == "ats_page":
    ats.ats_page()

elif st.session_state.page == "youtube_transcripter_page":
    youtubeTranscripter.youtube_transcripter_page()

elif st.session_state.page == "nutritionExpert_page":
    nutritionExpert.nutritionExpert_page()
