import streamlit as st

st.title("My First Streamlit Application")

st.image("profile.jpg",caption="Profile Picture",width=300)
st.header("Arit Kar")
st.write("### About")
st.text("Hello! I am a Btech Student and my major is computer Science ")
#st.markdown("[Linkdin Profile](https://www.linkedin.com/in/arit-kar-15b367239)")
if st.button("College"):
    st.write("Hertage Institute Of Technology")
st.sidebar.success("This is First page ")
year=st.slider("Which year are you in?",0,4,1)
st.write("I'm on ",year,"year")
