import streamlit as st

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# Function to handle page change
def change_page(page_name):
    st.session_state.page = page_name

# Sidebar for navigation
st.sidebar.title("Navigation")
if st.sidebar.button('Transcript'):
    change_page('Transcript')
if st.sidebar.button('Page 1'):
    change_page('Page 1')
if st.sidebar.button('Page 2'):
    change_page('Page 2')

# Display content based on selected page
if st.session_state.page == 'Transcript':
    st.title("Transcript")
    st.write("Transcript")
elif st.session_state.page == 'Page 1':
    st.title("Page 1")
    st.write("This is Page 1.")
elif st.session_state.page == 'Page 2':
    st.title("Page 2")
    st.write("This is Page 2 blah blah blah")