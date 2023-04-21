import streamlit as st
from predict_page import show_predict_page
from admin_predict_page import show_predict_page1

def page1():
    st.title('Model-1')
    show_predict_page()

def page2():
    st.title('Model-2')
    show_predict_page1()

pages = {
    'Model-1': page1,
    'Model-2': page2
}

# Define function to run app
def run_app():
    st.sidebar.title('Navigation')
    page = st.sidebar.radio('Go to', list(pages.keys()))

    # Call function associated with selected page
    pages[page]()

# Run the app
if __name__ == '__main__':
    run_app()

